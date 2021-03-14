"""
Contains convenient types to work with when attempting to work with
dns protocol.
"""
import re
from .exceptions import *
from socket import inet_aton
import re

class DnsQuery(object):
	"""
	Represents a parsed DNS query
	"""

	def __init__(self, query):
		# Parse the query
		parsed_query = _parse_query(query)

		# assign the header fields
		self.transaction_id = parsed_query[0]
		self.flags = parsed_query[1]
		self.questions = parsed_query[2]
		self.answer_rrs = parsed_query[3]
		self.authority_rrs = parsed_query[4]
		self.additional_rrs = parsed_query[5]
		self.name = parsed_query[6]
		self.dns_type = parsed_query[7]
		self.dns_class = parsed_query[8]

	def get_name(self):
		"""
		Returns a textual representation of the queried domain name
		"""
		return self.name[1:-1].decode().replace(
			'\x03', '.').replace('\x02', '.').replace('\x06', '.').\
			replace('\x08', '.')

	def __bytes__(self):
		return self.transaction_id + self.flags + self.questions + \
			   self.answer_rrs + self.authority_rrs + self.additional_rrs + \
			   self.name + self.dns_type + self.dns_class


class DnsResponse(object):
	"""
	Represents a DNS response
	"""
	def __init__(self, response):
		parsed_response = _parse_response(response)

		# assign header fields -> (transaction_id, flags, questions, answer_rrs,
		#						   authority_rrs, additional_rrs, name,
		#						   dns_type, dns_class, Answers)
		self.transaction_id = parsed_response[0]
		self.flags = parsed_response[1]
		self.questions = parsed_response[2]
		self.answer_rrs = parsed_response[3]
		self.authority_rrs = parsed_response[4]
		self.additional_rrs = parsed_response[5]
		self.name = parsed_response[6]
		self.dns_type = parsed_response[7]
		self.dns_class = parsed_response[8]
		self.answers = parsed_response[9]

	def __bytes__(self):
		return self.transaction_id + self.flags + self.questions + \
			   self.answer_rrs + self.authority_rrs + self.additional_rrs + \
			   self.name + self.dns_type + self.dns_class + \
			   b''.join(bytes(answer) for answer in self.answers)


class Answer(object):
	def __init__(self, answer):
		parsed_answer = _parse_answer(answer)

		# assign header fields -> (Name, Type, Class, TTL, Data length, address)
		self.name = parsed_answer[0]
		self.answer_type = parsed_answer[1]
		self.answer_class = parsed_answer[2]
		self.ttl = parsed_answer[3]
		self.data_length = parsed_answer[4]
		self.address = parsed_answer[5]

	def get_address(self):
		"""
		:return: Textual representation of the IP address
		"""
		return '.'.join(str(byte) for byte in self.address)

	def change_ip(self, ip_addr):
		"""
		Changes the answer IP
		:param ip_addr: ip address
		:type ip_addr: str
		:return: None
		"""
		# Validate IP address
		if not re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ip_addr):
			raise InvalidIPError
		if any(int(byte) > 255 for byte in ip_addr.split('.')):
			raise InvalidIPError

		self.address = inet_aton(ip_addr)

	def __bytes__(self):
		return self.name + self.answer_type + self.answer_class + self.ttl + \
			   self.data_length + self.address

	def __repr__(self):
		return self.get_address()


def _parse_query(query):
	"""
	Parses a DNS query

	:param query: DNS query to parse
	:return: (transaction_id, flags, questions, answer_rrs, authority_rrs,
	 		  additional_rrs, name, dns_type, dns_class)
	"""
	# Validate query
	name_ending = b'\x00' 	# Domain name ending
	if len(query) <= 12: raise InvalidQueryError
	if name_ending not in query[12:]: raise InvalidQueryError

	transaction_id = query[0:2]
	flags = query[2:4]
	questions = query[4:6]
	answer_rrs = query[6:8]
	authority_rrs = query[8:10]
	additional_rrs = query[10:12]
	name = query[12:query.find(name_ending, 12) + len(name_ending)]
	dns_type = query[-4:-2]
	dns_class = query[-2:]

	return (
		transaction_id,
		flags,
		questions,
		answer_rrs,
		authority_rrs,
		additional_rrs,
		name,
		dns_type,
		dns_class
	)


def _parse_answer(answer):
	"""
	Parses a specific answer from the dns response
	:param answer: answer to parse
	:return: (Name, Type, Class, TTL, Data length, address)
	"""
	name = answer[0:2]
	answer_type = answer[2:4]
	answer_class = answer[4:6]
	ttl = answer[6:10]
	data_length = answer[10:12]
	address = answer[12:]

	return (
		name,
		answer_type,
		answer_class,
		ttl,
		data_length,
		address
	)


def _parse_response(response):
	"""
	Parses a DNS response

	:return:(transaction_id, flags, questions, answer_rrs,
		     authority_rrs, additional_rrs, name,
		     dns_type, dns_class, Answers)
	"""
	answers = []
	new_answer_start = b'\xc0\x0c'
	while new_answer_start in response:
		index = response.rfind(new_answer_start)
		answers.append(Answer(response[index:]))
		response = response[:index]
	answers.reverse()
	return _parse_query(response) + (answers,)

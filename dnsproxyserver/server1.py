"""
The dns proxy server
"""
import socket
from .config import *
from .dnstypes import *
import datetime
def str2hex(stris):
	return ''.join([hex(c) for c in stris])
DNS_PORT = 53
DEFAULT_BUFFER_SIZE = 1024

class DnsServer(object):
	"""
	Represents the dns server
	"""
	def __init__(self, address, verbose=True):
		"""
		:param address: Socket address (Ip address, Port)
		:type address: tuple
		:param verbose:
		"""
		self.ip, self.port = address
		self.verbose = verbose

	def parse_query(self, query_data):
		name = query_data[12:query_data.find(b'\x00', 12)]
		next_length = ord(name[0])
		name_tmp = ''
		for mesenge in name[1:]:
			if next_length != 0:
				name_tmp += mesenge
				next_length -= 1
			else:
				next_length = ord(mesenge)
				name_tmp += '.'
		return name_tmp

	def parse_response(self, respone_data):
		name = respone_data[12:respone_data.find(b'\x00', 12)]
		next_length = ord(name[0])
		name_tmp = ''
		for mesenge in name[1:]:
			if next_length != 0:
				name_tmp += mesenge
				next_length -= 1
			else:
				next_length = ord(mesenge)
				name_tmp += '.'
		return name_tmp

	def run(self):
		# Used for getting responses from a real DNS server
		client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		client_socket.settimeout(100000)
		server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		server_socket.bind((self.ip, self.port))
		server_socket.settimeout(100000)

		if self.verbose:
			print('-' * 80)
			print('Starting DNS proxy server!\n'.center(80, ' '))
			print('--> Port: {}'.format(self.port))
			print('--> IP: {}'.format(self.ip))
			print('-' * 80)

		try:
			while True:
				# Get data from client
				(data, client_address) = server_socket.recvfrom(
					DEFAULT_BUFFER_SIZE)
				# Get response
				client_socket.sendto(data, (DEFAULT_DNS_SERVER,
													DNS_PORT))
				response = client_socket.recvfrom(DEFAULT_BUFFER_SIZE)[0]
				# Analyze data
				# Send response to the client
				server_socket.sendto(response, client_address)
				if self.verbose:
					print('{} Query for {} at {}'.format(
						client_address, self.parse_query(data), datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')))


		except KeyboardInterrupt:
			if self.verbose:
				print('\rServer Shutdown!')
		finally:
			if server_socket is not None: server_socket.close()
			if server_socket is not None: server_socket.close()
"""
The dns proxy server
"""
import socket
from config import *
from dnstypes import *

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
				query = DnsQuery(data)
				# Get response
				client_socket.sendto(query.__bytes__(), (DEFAULT_DNS_SERVER,
													DNS_PORT))
				response = client_socket.recvfrom(DEFAULT_BUFFER_SIZE)[0]
				response = DnsResponse(response)

				# Analyze data
				domain_name = query.get_name()
				if domain_name in DOMAIN_MAP.keys():
					# In case the domain is mapped
					if len(response.answers) > 2:
						# In case there is more than one answer, leave only one
						response.answer_rrs = b'\x00\x01'
						del response.answers[1:]
					response.answers[0].change_ip(DOMAIN_MAP[domain_name])


				# Send response to the client
				server_socket.sendto(response, client_address)
				if self.verbose:
					print('-' * 80)
					print('{} Asked for {} and received: \n{}'.format(
						client_address, query.get_name(), response.answers
					))
					print('-' * 80)


		except KeyboardInterrupt:
			if self.verbose:
				print('\rServer Shutdown!')
		finally:
			if server_socket is not None: server_socket.close()
			if server_socket is not None: server_socket.close()



server = DnsServer(('0.0.0.0', DNS_PORT))
server.run()
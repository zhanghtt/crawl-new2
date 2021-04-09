"""
The dns proxy server
"""
import socket
from .config import *
import datetime
import threading

DNS_PORT = 53
DEFAULT_BUFFER_SIZE = 102400
SEND_BUF_SIZE=4096
RECV_BUF_SIZE=4096


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
		self.state = None

		self.lock = threading.Lock()

		def receive_ation(passss):
			try:
				action_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				action_socket.bind((self.ip, 10053))
				action_socket.settimeout(100000)
				while True:
					(data, client_address) = action_socket.recvfrom(DEFAULT_BUFFER_SIZE)
					print('change state from {} to {}'.format(self.state, data))
					if data == b'None':
						self.state = None
					else:
						self.state = data
			except KeyboardInterrupt:
				if self.verbose:
					print('\rAction Server Shutdown!')
			finally:
				action_socket.close()

		thread = threading.Thread(target=receive_ation,args=(None,))
		thread.start()
		#thread.start_new_thread(receive_ation,(None,))

	def parse_query(self, query_data):
		name = query_data[12:query_data.find(b'\x00', 12)]
		name = str(name,'utf8')
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

		# -*- coding: UTF-8 -*-
		import socket
		import select

		server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		server_socket.bind((self.ip, self.port))
		server_socket.setblocking(False)
		client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		client_socket.setblocking(True)
		#client_socket.settimeout(T)
		inputs = [server_socket, client_socket]
		if self.verbose:
			print('-' * 80)
			print('Starting DNS proxy server!\n'.center(80, ' '))
			print('--> Port: {}'.format(self.port))
			print('--> IP: {}'.format(self.ip))
			print('-' * 80)

		def proxy(data, server_socket, client_socket):
			try:
				print("1")
				client_socket.sendto(data, (DEFAULT_DNS_SERVER, DNS_PORT))
				print("3")
				response = client_socket.recvfrom(DEFAULT_BUFFER_SIZE)[0]
				print("4")
				server_socket.sendto(response, client_address)
				print('action {} Query for {} at {}'.format(self.state, self.parse_query(data),
															datetime.datetime.now().strftime(
																'%Y-%m-%d %H:%M:%S.%f')))
			except:
				import traceback
				traceback.print_exc()
				print(5)

		while True:
			r_list, w_list, e_list = select.select(inputs, [], [], 1)
			for event in r_list:
				if event == server_socket:
					try:
						print("1")
						(data, client_address) = server_socket.recvfrom(DEFAULT_BUFFER_SIZE)
						print("2")
						client_socket.sendto(data, (DEFAULT_DNS_SERVER, DNS_PORT))
						print("3")
						response = client_socket.recvfrom(DEFAULT_BUFFER_SIZE)[0]
						print("4")
						server_socket.sendto(response, client_address)
						print('action {} Query for {} at {}'.format(self.state, self.parse_query(data),
																	datetime.datetime.now().strftime(
																		'%Y-%m-%d %H:%M:%S.%f')))
					except ConnectionResetError as e:
						import traceback
						traceback.print_exc()
						pass


server = DnsServer(('0.0.0.0', DNS_PORT))
server.run()
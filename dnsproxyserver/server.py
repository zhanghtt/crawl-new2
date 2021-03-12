"""
The dns proxy server
"""
import socket
from .config import *
from .dnstypes import *
import datetime
import threading
from mongo import op
import traceback

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
		self.writer = op.DBManger()

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
		# Used for getting responses from a real DNS server
		time_out = 50000
		time_out1 = 3
		client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		client_socket.settimeout(time_out1)
		client_socket.setsockopt(
			socket.SOL_SOCKET,
			socket.SO_SNDBUF,
			SEND_BUF_SIZE)
		client_socket.setsockopt(
			socket.SOL_SOCKET,
			socket.SO_RCVBUF,
			RECV_BUF_SIZE)
		server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		server_socket.bind((self.ip, self.port))
		server_socket.settimeout(time_out)
		server_socket.setsockopt(
			socket.SOL_SOCKET,
			socket.SO_SNDBUF,
			SEND_BUF_SIZE)
		server_socket.setsockopt(
			socket.SOL_SOCKET,
			socket.SO_RCVBUF,
			RECV_BUF_SIZE)

		if self.verbose:
			print('-' * 80)
			print('Starting DNS proxy server!\n'.center(80, ' '))
			print('--> Port: {}'.format(self.port))
			print('--> IP: {}'.format(self.ip))
			print('-' * 80)

		try:
			while True:
				# Get data from client
				while True:
					try:
						(data, client_address) = server_socket.recvfrom(DEFAULT_BUFFER_SIZE)
						break
					except:
						traceback.print_exc()
						# if server_socket is not None: server_socket.close()
						# server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
						# server_socket.bind((self.ip, self.port))
						# server_socket.settimeout(time_out)
						pass
				# Get response
				while True:
					try:
						client_socket.sendto(data, (DEFAULT_DNS_SERVER, DNS_PORT))
						response = client_socket.recvfrom(DEFAULT_BUFFER_SIZE)[0]
						break
					except:
						traceback.print_exc()
						print("resendto client_socket")
						if client_socket is not None: client_socket.close()
						client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
						client_socket.settimeout(time_out1)
						pass

				# Analyze data
				# Send response to the client
				while True:
					try:
						server_socket.sendto(response, client_address)
						break
					except:
						traceback.print_exc()
						print("resendto server_socket")
						if server_socket is not None: server_socket.close()
						server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
						server_socket.bind((self.ip, self.port))
						server_socket.settimeout(time_out)
						pass
				if self.verbose:
					# print('{} action {} Query for {} at {}'.format(
					# 	client_address, self.state, self.parse_query(data), datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')))
					print('action {} Query for {} at {}'.format(self.state, self.parse_query(data),
																datetime.datetime.now().strftime(
																	'%Y-%m-%d %H:%M:%S.%f')))
					if self.state and self.state != 'None' and self.state != 'none':
						action_info = self.state.decode('utf8').split("_")
						self.writer.insert_one_dict(db_collect=("jicheng", "autopkgcatpure"),
													data_dict={"app_id": action_info[1], 'action_id': action_info[3],
															   'session_id': action_info[4],
															   'host': self.parse_query(data),
															   'time': datetime.datetime.now().strftime(
																   '%Y-%m-%d %H:%M:%S.%f')
														, 'app_name': action_info[5], 'platform': action_info[6],'devicename':action_info[7],'udid':action_info[8]})

		except KeyboardInterrupt:
			if self.verbose:
				print('\rServer Shutdown!')
		finally:
			if client_socket is not None: client_socket.close()
			if server_socket is not None: server_socket.close()




server = DnsServer(('0.0.0.0', DNS_PORT))
server.run()
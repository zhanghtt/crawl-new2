"""
This script is the server itself. In order to run the server you must run this
script
"""
from dnsproxy.server1 import *

def main():
	server = DnsServer(('0.0.0.0', DNS_PORT))
	server.run()

if __name__ == '__main__':
	main()

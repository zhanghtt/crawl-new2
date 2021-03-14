"""
This file contains all the dns proxy server configuration

"""
# Default ip that blocked websites will be referenced to
DEFAULT_IP = '127.0.0.1'

# Maps between specific queried domain name and ip
DOMAIN_MAP = {
    'www.facebook.com': DEFAULT_IP
}

# The DNS server that will be used in order to answer unmapped queries
DEFAULT_DNS_SERVER = '192.168.50.1'

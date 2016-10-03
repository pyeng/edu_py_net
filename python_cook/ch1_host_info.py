#!/usr/bin/env python

import socket

def print_machine_info():
	host_name = socket.gethostname()
	ip_addr = socket.gethostbyname(host_name)
	print "Hostname: %s" % host_name
	print "IP address: %s" % ip_addr

if __name__ == "__main__" :
	print_machine_info()
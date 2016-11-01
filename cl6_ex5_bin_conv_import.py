#!/usr/bin/env python

from cl6_ex3_ip_valid import ip_valid
from cl6_ex4_def_dec_bin_conv import dec_bin_conv

ip_addr = raw_input("\nInput an IP address: ")

check = "not valid"
if ip_valid(ip_addr):
	check = "valid"
	bin = dec_bin_conv(ip_addr)
	print "\nIP address %s is %s" % (ip_addr, check)
	print "And the binary form of %s is %s\n" % (ip_addr, bin)
else:
	print "\nYou entered an invalid IP address!\n"
	
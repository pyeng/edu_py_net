#!/usr/bin/env python

import sys

if len(sys.argv) != 2:
	#Exit script
	sys.exit("Usage: ./cl3_ex1_dec_bin_conv_arg.py <ip_address>")

binary = [ ]

ip_addr = sys.argv.pop()
octets = ip_addr.split(".")

if len(octets) != 4:
	sys.exit("Invalid IP address entered")

for i in octets:
	i = bin(int(i))[2:]
	
	while True:
		if len(i) >= 8:
			break
		i = "0" + i

	binary.append(i)
	bin_oct = ".".join(binary)

#print bin_oct

print "\n%-20s %-20s" % ("IP address", "Binary")
print "%-20s %-20s\n" % (ip_addr, bin_oct)
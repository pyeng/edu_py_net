#!/usr/bin/env python

def dec_bin_conv(ip_addr):
	import sys
	binary = []

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
	return bin_oct
#	print "\n%-20s %-20s" % ("IP address", "Binary")
#	print "%-20s %-20s\n" % (ip_addr, bin_oct)

#ip_address = "10.1.0.1"
#dec_bin_conv(ip_address)
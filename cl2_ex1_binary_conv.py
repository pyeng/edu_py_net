#!/usr/bin/env python

ip_addr = raw_input("\nInput an IP address: ")

octets = ip_addr.split(".")

if len(octets) == 3:
	octets.append("0")
elif len(octets) == 4:
	octets[3] = "0"

bin_first = bin(int(octets[0]))
hex_first = hex(int(octets[0]))
net_num = ".".join(octets)

print "\nYour IP network is %s" % net_num
print "\n\n"
print "%-20s %-20s %-20s" % ("NETWORK_NUMBER", "FIRST_OCTET_BINARY", "FIRST_OCTET_HEX")
print "%-20s %-20s %-20s" % (net_num, bin_first, hex_first)
print  "\n\n"
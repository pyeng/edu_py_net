#!/usr/bin/env python

ip_addr = raw_input("\nInput an IP address: ")

octets = ip_addr.split(".")

first_octet = bin(int(octets[0]))
second_octet = bin(int(octets[1]))
third_octet = bin(int(octets[2]))
fourth_octet = bin(int(octets[3]))

print "\n%-15s %-15s %-15s %-15s" % ("first_octet", "second_octet", "third_octet", "fourth_octet")
print "%-15s %-15s %-15s %-15s" % (first_octet, second_octet, third_octet, fourth_octet)
print "\n"


#print octets
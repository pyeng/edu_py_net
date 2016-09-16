#!/usr/bin/env python

ipv6_addr = "FE80:0000:0000:0000:0101:A3EF:EE1E:1719"

ipv6_split = ipv6_addr.split(":")

print 
print "IPv6 address split:"
print ipv6_split
print

ipv6_new = ":".join(ipv6_split)

print "IPv6 address re-joined:"
print ipv6_new
print
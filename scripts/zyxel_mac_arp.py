#!/usr/bin/env python

mac_addr = """
6         1              00:19:e0:74:15:1f   Dynamic   
6         1              00:1e:58:9e:c0:e1   Dynamic   
6         1              00:1e:58:a9:25:38   Dynamic   
6         1              00:21:27:ef:81:72   Dynamic   
6         1              d0:50:99:60:d3:fa   Dynamic   
6         1              f4:f2:6d:5c:0d:c5   Dynamic    
"""
mac_split = (mac_addr.strip("\n")).split("\n")
print "\n"
for line in mac_split:
	line =  line.split()
	mac = line[2]
	#(port, vlan, mac, typ) = line
	mac = mac.split(":")
	mac_new =  "%s%s.%s%s.%s%s" % (mac[0], mac[1], mac[2], mac[3], mac[4], mac[5])

	print "sh arp | in %s" % mac_new
print "\n"
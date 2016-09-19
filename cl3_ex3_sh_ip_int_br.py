#!/usr/bin/env python

import pprint

show_ip_int_brief = '''
Interface            IP-Address      OK?     Method      Status     Protocol
FastEthernet0   unassigned      YES     unset          up          up
FastEthernet1   unassigned      YES     unset          up          up
FastEthernet2   unassigned      YES     unset          down      down
FastEthernet3   unassigned      YES     unset          up          up
FastEthernet4    6.9.4.10          YES     NVRAM       up          up
NVI0                  6.9.4.10          YES     unset           up          up
Tunnel1            16.25.253.2     YES     NVRAM       up          down
Tunnel2            16.25.253.6     YES     NVRAM       up          down
Vlan1                unassigned      YES    NVRAM       down      down
Vlan10              10.220.88.1     YES     NVRAM       up          up
Vlan20              192.168.0.1     YES     NVRAM       down      down
Vlan100            10.220.84.1     YES     NVRAM       up          up
'''

show_ip_list = []

show_ip_int_brief = (show_ip_int_brief.strip("\n")).split("\n")

for i in show_ip_int_brief:
	
	if "Interface" in i:
		continue
	i = i.split()
	if len(i) == 6:
	
		(iface, ip_addr, ok, method, status, protocol) = i
		
		if (status == "up") and (protocol == "up"):
			show_ip_list.append((iface, ip_addr, status, protocol))

print "\n"
pprint.pprint(show_ip_list)
#print show_ip_list
print "\n"
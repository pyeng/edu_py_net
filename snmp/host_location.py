#!/usr/bin/env python

import sys

from snmp_helper import snmp_get_oid,snmp_extract

if len(sys.argv) != 2:
	#Exit script
	sys.exit("Usage: ./host_location.py <SNMP Community>")

switch = (
    "192.168.12.1",
    "192.168.12.2",
    "192.168.12.3",
    "192.168.12.4",
    "192.168.12.5",
 	)

COMMUNITY_STRING = sys.argv.pop()
SNMP_PORT = 161
device = (switch, COMMUNITY_STRING, SNMP_PORT)

for i in switch:
	device = (i, COMMUNITY_STRING, SNMP_PORT)
	snmp_hostname = snmp_get_oid(device, oid='1.3.6.1.2.1.1.5.0', display_errors=True)
	snmp_location = snmp_get_oid(device, oid='1.3.6.1.2.1.1.6.0', display_errors=True)
	hostname = snmp_extract(snmp_hostname)
	location = snmp_extract(snmp_location)

	print "%-15s %-8s %-8s" % (i, hostname, location)
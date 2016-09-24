#!/usr/bin/env python

from snmp_helper import snmp_get_oid,snmp_extract

switch = (192.168.12.1,	192.168.12.90, 192.168.12.42, 192.168.12.101)

COMMUNITY_STRING = 'SnNeMtP'
SNMP_PORT = 161
device = (switch, COMMUNITY_STRING, SNMP_PORT)

for i in switch:
	snmp_data = snmp_get_oid(device, oid='1.3.6.1.2.1.1.5.0', display_errors=True)

	output = snmp_extract(snmp_data)

print "%s, %s" % (switch, output)
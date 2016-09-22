#!/usr/bin/env python

import pprint

from cdp_data import (sw1_show_cdp_neighbors, sw1_show_cdp_neighbors_detail, \
r1_show_cdp_neighbors, r1_show_cdp_neighbors_detail, \
r2_show_cdp_neighbors, r2_show_cdp_neighbors_detail, \
r3_show_cdp_neighbors, r3_show_cdp_neighbors_detail, \
r4_show_cdp_neighbors, r4_show_cdp_neighbors_detail, \
r5_show_cdp_neighbors, r5_show_cdp_neighbors_detail)

cdp_neighbors = (
    sw1_show_cdp_neighbors_detail, 
    r1_show_cdp_neighbors_detail, 
    r2_show_cdp_neighbors_detail, 
    r3_show_cdp_neighbors_detail, 
    r4_show_cdp_neighbors_detail, 
    r5_show_cdp_neighbors_detail, 
)

# Initialize network_devices
network_devices = {}

for cdp_ent in cdp_neighbors:
	cdp_ent = cdp_ent.strip("\n").split("\n")
	for i in cdp_ent:
		if "Device ID: " in i:
			hostname = i.split("Device ID: ")[1]
			network_devices[hostname] = {}
		if "IP address: " in i:
			ip_addr = i.split("IP address: ")[1]
			network_devices[hostname]["ip"] = ip_addr
		if "Platform: " in i:
			model = (i.split(",")[0]).split(" ")[-1]
			network_devices[hostname]["model"] = model
			vendor = (i.split(",")[0]).split(" ")[-2]
			network_devices[hostname]["vendor"] = vendor
			if "Router" in i:
				device_type = "router"
			elif "Switch" in i:
				device_type = "switch"
			else:
				device_type = "unknown"
			network_devices[hostname]["device_type"] = device_type

pprint.pprint(network_devices)

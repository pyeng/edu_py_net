#!/usr/bin/env python

import pprint

from cdp_data import (
	sw1_show_cdp_neighbors, sw1_show_cdp_neighbors_detail, 
	r1_show_cdp_neighbors, r1_show_cdp_neighbors_detail, 
	r2_show_cdp_neighbors, r2_show_cdp_neighbors_detail, 
	r3_show_cdp_neighbors, r3_show_cdp_neighbors_detail, 
	r4_show_cdp_neighbors, r4_show_cdp_neighbors_detail, 
	r5_show_cdp_neighbors, r5_show_cdp_neighbors_detail
	)

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

	# Reset hostname for each cdp output
	#remote_host = ""
	#local_host = ""

	for i in cdp_ent:

		if "show cdp neighbors detail" in i:
			local_host = i.split("show cdp neighbors detail")[0]
			if ">" in local_host:
				local_host = local_host.split(">")[0]
			elif "#" in local_host:
				local_host = local_host.split("#")[0]
			else:
				sys.exit(Invalid prompt)

			print local_host


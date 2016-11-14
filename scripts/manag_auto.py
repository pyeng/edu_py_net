#!/usr/bin/env python

import os
import multiprocessing
import subprocess
import ipaddress
import pprint
import re
from snmp_helper import snmp_get_oid,snmp_extract

manag_net = ipaddress.ip_network(u"10.90.90.0/24")

oid_model = ".1.3.6.1.2.1.1.1.0"
oid_hostname = ".1.3.6.1.2.1.1.5.0"
oid_location = ".1.3.6.1.2.1.1.6.0"

DNULL = open(os.devnull, 'w')


def data_from_snmp(switch_ip, oid):
    COMMUNITY_STRING = 'SnNeMtP'
    SNMP_PORT = 161

    switch = (switch_ip, COMMUNITY_STRING, SNMP_PORT)
    snmp_data = snmp_get_oid(switch, oid, display_errors=True)
    output = snmp_extract(snmp_data).split()[:2]
    return output


def action(host,mp_queue):
    response = subprocess.call(["ping", "-c", "2", "-w", '2', host], stdout=DNULL)
    if response == 0:
    	hostname = data_from_snmp(host, oid_hostname)
        location = data_from_snmp(host, oid_location)
        vendor = data_from_snmp(host, oid_model)
        print host, hostname, location, vendor
        result = True
    else:
        #print host, 'is down!'
        result = False
    mp_queue.put((result,host))

def worker(manag_net):
    mp_queue = multiprocessing.Queue()
    processes = []
    for device in manag_net.hosts():
    	device = str(device)
    	gw = re.search(r"(\.1)$", device)
        if gw:
            print 
        else:
            p = multiprocessing.Process(target=action, args=(device, mp_queue))
            processes.append(p)
            p.start()
    for p in processes:
        p.join()
    results = {True:[], False:[]}
    for p in processes:
       key, value =  mp_queue.get()
       results[key] += [value]
    return results[True], results[False]

success, failed = worker(manag_net)

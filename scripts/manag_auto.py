#!/usr/bin/env python

import os
import multiprocessing
import subprocess
import ipaddress
from snmp_helper import snmp_get_oid,snmp_extract

manag_net = ipaddress.ip_network(u"192.168.20.64/29")

DNULL = open(os.devnull, 'w')

def data_from_snmp(switch_ip):
    COMMUNITY_STRING = 'SnNeMtP'
    SNMP_PORT = 161
    used_ports = 0

    oid_model = ".1.3.6.1.2.1.1.1.0"
    oid_hostname = ".1.3.6.1.2.1.1.5.0"
    oid_location = ".1.3.6.1.2.1.1.6.0"

    switch = (switch_ip, COMMUNITY_STRING, SNMP_PORT)
    snmp_data = snmp_get_oid(switch, oid_model, display_errors=True)
    model = snmp_extract(snmp_data)
    return model


def ping(host,mp_queue):
    response = subprocess.call(["ping", "-c", "2", "-w", '2', host], stdout=DNULL)
    if response == 0:
    	dev = data_from_snmp(host)
        print host, dev
        result = True
    else:
        print host, 'is down!'
        result = False
    mp_queue.put((result,host))

def worker(manag_net):
    mp_queue = multiprocessing.Queue()
    processes = []
    for device in manag_net.hosts():
    	device = str(device)
    	
        p = multiprocessing.Process(target=ping, args=(device, mp_queue))
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

#success = worker(manag_net)
"""
>>> addr4 = ipaddress.ip_address(u"192.168.2.1")
>>> addr4 in net4
True

>>> str(addr4)
'192.168.2.1'
"""
#!/usr/bin/env python

import ntplib
from time import ctime

def print_time():
	ntp_client = ntplib.NTPClient()
	responce = ntp_client.request("pool.ntp.org")
	print ctime(responce.tx_time)

if __name__ == "__main__":
	print_time()
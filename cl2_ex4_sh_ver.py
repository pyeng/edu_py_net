#!/usr/bin/env python

cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), \
Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"

ios_version = cisco_ios.split(",")
ios_version = ios_version[2].split(" Version ")[1]

print "ios_version = %s" % ios_version
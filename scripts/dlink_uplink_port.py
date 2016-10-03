#!/usr/bin/env python

import telnetlib

host = "192.168.22.190"
user = "admin"
password = "password"
command = "show iproute"
disclip = "disable clipaging"
enclip = "enable clipaging"

tn = telnetlib.Telnet(str(host),23,1)
tn.read_until("NeverMatches",0.5)
tn.write(user + "\n")
tn.read_until("NeverMatches",0.5)
tn.write(password + "\n")
tn.read_until("NeverMatches",0.5)
tn.write(disclip + "\n")
tn.read_until("NeverMatches",0.5)
tn.write(command + "\n")

ipif = tn.read_until("NeverMatches",0.5)
for i in ipif.split("\n"):
    if "IP Address" in i:
        i = i.split(":")[1]
        (ip_addr, typ) = i
        print ip_addr



tn.write(enclip + "\n")
tn.read_until("NeverMatches",0.5)
#tn.write("save\n")
#tn.read_until("NeverMatches",5)
tn.write("logout\n")
tn.read_until("NeverMatches",0.5)
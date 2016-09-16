#!/usr/bin/env python

import fileinput

for line in fileinput.input():
    line = line.strip()
    print line.split(".")
    #print line.strip("\n")

#echo '192.168.1.1'  | ./test3.py 
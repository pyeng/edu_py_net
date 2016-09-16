#!/usr/bin/env python

import fileinput

for line in fileinput.input():
    line = line.strip()
    print line.split(".")

#echo '192.168.1.1'  | ./test3.py 
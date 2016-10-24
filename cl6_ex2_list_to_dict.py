#!/usr/bin/env python
"""
def convert_list_dict(data):
	a_dict = {}
	x = 0
	for i in data:
		if x <= len(data):
			a_dict[x] = data[x]
			x += 1
	return a_dict

a_list = [1, 2, 3, "hello", "world"]

new_dict = convert_list_dict(a_list)

print
print "List: %s" % a_list
print "Dict: %s" % new_dict
print
"""

def convert_list_dict(data):
 
    new_dict = {}

    for i, v in enumerate(data):
        new_dict[i] = v

    return new_dict

a_list = [1, 2, 3, "hello", "world"]

test_dict = convert_list_dict(a_list)

print
print "List: %s" % a_list
print "Dict: %s" % test_dict
print
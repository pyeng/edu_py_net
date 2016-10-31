#!/usr/bin/env python
"""
3a.Convert the IP address validation code (Class4, exercise1)
into a function, take one variable 'ip_address' and return 
either True or False (depending on whether 'ip_address' is 
a valid IP). Only include IP address checking in 
the function--no prompting for input, no printing to standard 
output.


3b. Import this IP address validation function into the Python 
interpreter shell and test it (use both 'import x' and 
'from x import y').
"""
"""
ip_address = "10.100.0.1"
ip_split = ip_address.split(".")
first_octet = ip_split[0]

if len(ip_split) == 4:
	if 1 < int(first_octet) < 223:
		if int(first_octet) != 127:
			if ip_split[0:2] != ["169", "254"]:
				for octet in ip_split[1:4]
"""
def ip_valid(ip_address):

	 # Make sure IP has four octets
	 octets = ip_address.split(".")
	 if len(octets) != 4:
	 	return False

	 # convert octet from string to int
	 for i, octet in enumerate(octets):
	 	try:
	 		octets[i] = int(octet)
	 	except ValueError:
	 		# couldn't convert octet to an integer
	 		return False

	 # map variables to elements of octets list
	 first_octet, second_octet, third_octet, fourth_octet = octets

	 # Check first_octet meets conditions
	 if first_octet < 1:
	 	return False
	 elif first_octet > 223:
	 	return False
	 elif first_octet == 127:
	 	return False

	 # Check 169.254.X.X condition
	 if first_octet == 169 and second_octet == 254:
	 	return False

	 # Check 2nd - 4th octets
	 for octet in (second_octet, third_octet, fourth_octet):
	 	if (octet < 0) or (octet > 255):
	 		return False

	 # Passed all of the checks
	 return True


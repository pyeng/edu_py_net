#!/usr/bin/env python

def multi_func(x,y,z=3):
	print x, y, z

# the function with all positional arguments
multi_func(1,2,3)

#the function with all named argument
multi_func(y=2,z =3, x=1)

#the function with a mix of positional and named arguments
multi_func(1, z=3, y=2)

#function with only two arguments and use the default value for z.
multi_func(1,2)
#!/usr/bin/python3
"""adds two integers"""

def add_integer(a, b=98):
	"""adds int a, b.
	float arguments are typecasted into int before addition is perfomed
	Raises:
		TypeError: if either a or b ia a non-integer or non-float
	"""
	if((not isinstance(a, int) and not isinstance(a, float))):
		raise TypeError("a must be an integer or b must be an integer")
	if ((not isinstance(b, int) and not isinstance(b, float))):
		raise TypeError("b must be an integer")
	return(int(a) + int(b))

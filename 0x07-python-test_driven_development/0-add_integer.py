def add_integer(a, b=98):
	"""function that return the addition of a and b

	Args:
	    a (int): integer value a
	    b (int, optional): integer value b. Defaults to 98.
	
	return: return a + bx
	"""
	if type(a) is not int:
		raise("a must be an integer")
	if type(b) is not int:
		raise("b must be an integer")
	a = int(a)
	b = int(b)
	return (a + b)
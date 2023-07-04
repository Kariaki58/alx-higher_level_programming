def add_integer(a, b=98):
    """function that return the addition of a and b
    Args:
    a(int): integer value a
    b(int, optional): integer value b. Dfaults to 98.
    return: return a + b
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return (a + b)

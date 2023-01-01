#!/usr/bin/python3
"""

This is function to add two numbers

"""


def add_integer(a, b=98):
    """Function to add two integer or float together
    
    Args: 
    	a: first number
	b: second number

    Returns: 
    	The result of addition of a and b
    
    Raises:
    	TypeError: if a and b are not integer or float
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)

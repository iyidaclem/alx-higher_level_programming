#!/usr/bin/python3

def safe_print_integer(value):
    """Print integer with "{:d}".format().
    Args:
        value (int): Integer to print.
    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):

#!/usr/bin/python3
def safe_print_division(a, b):
    r = None
    try:
        r = a/b
        print("Inside result: {}".format(r), end="\n")
    except (ValueError, TypeError, ZeroDivisionError):
        print("Inside result: {}".format(r), end="\n")
    finally:
        print("{} / {} = {}".format(a, b, r), end="\n")
        return (r)

#!/usr/bin/python3
"""Defines a function that check if if object is instance of a class"""


def is_same_class(obj, a_class):
    """
    Checks if obj is instance of a_class

    Args:
        object: The object in question
        a_class: The class in question
    Returns: True if is instance and false if not
    """
    return type(obj) == a_class)

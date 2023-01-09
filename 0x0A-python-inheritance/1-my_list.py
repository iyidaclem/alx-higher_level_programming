#!/usr/bin/python3
"""Inherits from lists"""


class MyList(list):
    """child class inheriting from list class"""

    def print_sorted(self):
        """print the list in a sorted order - ascending"""
        print(sorted(self))

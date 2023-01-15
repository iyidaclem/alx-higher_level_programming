#!/usr/bin/python3
"""This module houses the base model for the entire project"""


class Base:
    """ Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the class
        Args:
            id: Id of the new instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

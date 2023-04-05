#!/usr/bin/python3
"""find the peak of a list"""


def find_peak(my_list):
    """Function that finds the peak of a list"""

    if my_list == [] or my_list == None:
        return
    first = 0
    last = len(my_list) - 1

    while first < last:
        middle = (first + last) // 2

        if my_list[middle] < my_list[middle+1]:
            first = middle + 1
        else:
            last = middle

    return my_list[first]

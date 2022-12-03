#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not my_list:
        pass
    a = list.copy(my_list)
    a[idx] = element
    return (a)

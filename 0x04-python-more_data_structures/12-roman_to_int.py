#!/usr/bin/python3
import re


def roman_to_int(roman_string):
    if not roman_string:
        return 0
    pattern = re.compile(r"""
                          ^M{0,3}
                          (CM|CD|D?C{0,3})?
                          (XC|XL|L?X{0,3})?
                          (IX|IV|V?I{0,3})?$
            """, re.VERBOSE)
    if re.match(pattern, roman_string.upper()):
        pass
    else:
        return 0
    roman_table = {"I": 1, "V": 5, "X": 10,
                   "L": 50, "C": 100, "D": 500,
                   "M": 1000}
    total = 0
    prev = 0
    rep = 0
    roman_string = roman_string.upper()
    for j in roman_string:
        if j in roman_table:
            if prev < roman_table[j]:
                total += roman_table[j] - (prev * 2)
                prev = roman_table[j]
            else:
                total += roman_table[j]
                prev = roman_table[j]
        else:
            return 0
    return total

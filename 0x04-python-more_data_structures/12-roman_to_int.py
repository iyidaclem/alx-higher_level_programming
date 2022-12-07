#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return None
    roman_table = {"I": 1, "V": 5, "X": 10,
                   "L": 50, "C": 100, "D": 500,
                   "M": 1000}
    total = 0
    prev = 0
    roman_string = roman_string.upper()
    for j in roman_string:
        if j in roman_table:
            if prev < roman_table[j]:
                total += roman_table[j] - prev
                prev = roman_table[j]
            else:
                total += roman_table[j]
                prev = roman_table[j]
        else:
            return None
    return total

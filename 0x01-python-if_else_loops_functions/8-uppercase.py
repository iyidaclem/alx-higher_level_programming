#!/usr/bin/python3
def uppercase(str):
    num = ord(str)
    if (num >= 97 and num <= 122):
        upper = chr((num - 97) + 65)
    else:
        upper = str
    print(f"{upper}")

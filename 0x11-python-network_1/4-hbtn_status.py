#!/usr/bin/python3
"""
Write a Python script that fetches https://alx-intranet.hbtn.io/status
using requests package
"""
import requests


if __name__ == "__main__":
    res = requests.get('https://intranet.hbtn.io/status')
    txt = res.text
    print('Body response:\n\t- type: {}\n\t- content: {}'
          .format(type(txt), txt))

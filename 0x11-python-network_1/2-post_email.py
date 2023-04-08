#!/usr/bin/python3
"""
script thati:
    takes in a URL and an email,
    sends a POST request to the passed URL with the email as a paramete
    and displays the body of the res (decoded in utf-8)
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(val).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as res:
        print(res.read().decode("utf-8"))

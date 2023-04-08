#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the
letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    content = {'q': ""}

    try:
        content['q'] = sys.argv[1]
    except:
        pass

    res = requests.post('http://0.0.0.0:5000/search_user', content)

    try:
        json_o = res.json()
        if not json_o:
            print("No result")
        else:
            print("[{}] {}".format(json_o.get('id'), json_o.get('name')))
    except:
        print("Not a valid JSON")

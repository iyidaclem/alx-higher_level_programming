#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/users/{}'.format(sys.argv[1])
    headers = {'Accept': 'application/vnd.github+json',
               'Authorization': 'Bearer {}'.format(sys.argv[2]),
               'X-GitHub-Api-Version': '2022-11-28'}
    r = requests.get(url, headers=headers)
    data = r.json()
    print("{}".format(data.get('id')))

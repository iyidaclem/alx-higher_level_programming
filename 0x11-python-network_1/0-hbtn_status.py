#!/usr/bin/python3
""" Python script that fetches from the url https://intranet.hbtn.io/status """


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        data = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- data: {}".format(data))
        print("\t- utf8 data: {}".format(data.decode('utf-8')))

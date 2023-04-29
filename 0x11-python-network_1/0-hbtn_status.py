#!/usr/bin/python3
""" using urllib packages, write a script that fetches https://alx-intranet.hbtn.io/status
"""
import urlib.requests


if __name__ == '__main__': 
    request = urlib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))

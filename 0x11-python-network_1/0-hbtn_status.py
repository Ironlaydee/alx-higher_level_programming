#!/usr/bin/python3
""" using urllib packages, write a script that fetches 'https://alx-intranet.hbtn.io/status'
"""
import urlib packages


if __name__ == '__main__': 
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- comtent: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))

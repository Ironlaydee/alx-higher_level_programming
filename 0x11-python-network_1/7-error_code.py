#!/usr/bin/python3
""" a script that takez in the URL
sends a request to the URL
displays the body of the response
"""

import sys
import responses


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
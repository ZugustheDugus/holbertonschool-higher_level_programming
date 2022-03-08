#!/usr/bin/python3
"""
Script to fetch a url
"""

import urllib.request

if __name__ == '__main__':

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as resp:
        html = resp.read()

    print("Body response:")
    print("\t- type: " + str(type(html)))
    print("\t- content: " + str(html))
    print("\t- utf8 content: " + str(html.decode('utf8')))



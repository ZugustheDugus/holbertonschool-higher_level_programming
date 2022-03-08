#!/usr/bin/python3
"""
Script to fetch a url
"""

import urllib.request

def rqst0():
    """Function to fetch the url"""

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()

    print("Body response:")
    print("\t- type: " + str(type(html)))
    print("\t- content: " + str(html))
    print("\t- utf8 content: " + str(html.decode('utf8')))

if __name__ == '__main__':
    rqst0()

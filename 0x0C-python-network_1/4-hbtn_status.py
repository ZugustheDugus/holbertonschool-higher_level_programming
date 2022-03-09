#!/usr/bin/python3
"""
Script to fetch https://intranet.hbtn.io/status
"""


if __name__ == '__main__':
    import requests

    rqst = requests.get('https://intranet.hbtn.io/status')

    print("Body response:")
    print("\t- type: {}".format(type(rqst.text)))
    print("\t- type: {}".format(rqst.text))

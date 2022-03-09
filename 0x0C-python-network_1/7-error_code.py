#!/usr/bin/python3
"""
Script to catch HTTPS errors
"""

if __name__ == '__main__':
    import requests
    import sys

    rqst = requests.get(sys.argv[1])
    if rqst.status_code < 400:
        print(rqst.text)
    else:
        print("Error code: {}".format(rqst.status_code))

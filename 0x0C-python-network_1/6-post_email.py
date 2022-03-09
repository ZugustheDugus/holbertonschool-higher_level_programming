#!/usr/bin/python3
"""
POST request to email
"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    eml = {'email': sys.argv[2]}
    rqst = requests.post(url, data=eml)

    print(rqst.text)

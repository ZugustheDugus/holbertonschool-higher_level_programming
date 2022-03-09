#!/usr/bin/python3
"""
Script to display Github ID
"""

if __name__ == '__main__':
    import requests
    from requests.auth import HTTPBasicAuth
    import sys

    tok = sys.argv[2]
    usr = sys.argv[1]
    url = "https://api.github.com/user"

    rqst = requests.get(url, auth=HTTPBasicAuth(usr, tok)).json()
    print(rqst.get('id'))

#!/usr/bin/python3
"""
Script totake URL, send request, and display the value of X-Request Id
"""

if __name__ == '__main__':
    import requests
    import sys

    rqst = requests.get(sys.argv[1])
    print(rqst.headers.get('X-Request-Id'))
#!/usr/bin/python3
"""
Script to take a URL and send a request to display the value of
X-Request-ID
"""


if __name__ == '__main__':
    import urllib.request
    import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    html = response.info()

print(html.get('X-request-ID'))
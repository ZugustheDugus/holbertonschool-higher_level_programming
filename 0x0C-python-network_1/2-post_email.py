#!/usr/bin/python3
"""
Take URL and email and send a post request to the URL
with email as the parameter
"""


if __name__ == '__main__':

    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    val = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(val)
    data = data.encode('UTF-8')
    rqst = urllib.request.Request(url, data)
    with urllib.request.urlopen(rqst) as response:
        _pge = response.read()

    print(_pge.decode('UTF-8'))

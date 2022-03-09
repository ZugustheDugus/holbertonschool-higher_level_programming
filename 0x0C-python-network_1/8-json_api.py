#!/usr/bin/python3
"""
Script to catch HTTP errors
"""

if __name__ == '__main__':
    import requests
    import sys

    if len(sys.argv) < 2:
        tmp = ""
    else:
        tmp = sys.argv[1]

    eml = {'q': tmp}
    rqst = requests.post('http://0.0.0.0:5000/search_user', data=eml)

    try:
        jason = rqst.json()
        if len(jason) == 0:
            print("No result")
        else:
            print("[{}] {}".format(jason['id'], jason['name']))
    except:
        print("Not a valid JSON")

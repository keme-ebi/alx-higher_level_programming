#!/usr/bin/python3
"""
sends a request to the url and displays the body of the response
if the http status code >= 400, it prints 'Error code: ' followed by the
value of the http status code
"""
import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]
    req = requests.get(url)
    if req.status_code >= 400:
        print('Error code: {}'.format(req.status_code))
    else:
        print(req.text)

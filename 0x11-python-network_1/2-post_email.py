#!/usr/bin/python3
"""
sends a POST request to the passed url and displays the body of the response
decoded in utf-8
"""
import sys
import urllib.request
import urllib.parse


if __name__ == '__main__':
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email).encode()
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        mail = response.read().decode('utf-8')
    print(mail)

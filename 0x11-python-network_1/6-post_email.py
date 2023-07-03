#!/usr/bin/python3
"""
sends a POST request to the passed url and displays the body of the response
"""
import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    req = requests.post(url, data=email)
    print(req.text)

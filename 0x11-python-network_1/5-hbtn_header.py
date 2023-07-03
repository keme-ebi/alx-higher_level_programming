#!/usr/bin/python3
"""
sends a request to a url and displays the value of the variable X-Request-Id
"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    resp = requests.get(url)
    head = resp.headers.get('X-Request-Id')
    print(head)

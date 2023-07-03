#!/usr/bin/python3
"""
sends a request to the url and displays the response
"""
import urllib.request
import sys
import urllib.error


if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            resp = response.read().decode('utf-8')
        print(resp)
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))

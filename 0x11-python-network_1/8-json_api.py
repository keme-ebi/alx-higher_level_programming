#!/usr/bin/python3
"""
sends a post request to a url with letter as a parameter
"""
import sys
import requests


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    value = {'q': letter}
    req = requests.post(url, data=value)
    try:
        json = req.json()
        if json:
            print('[{}] {}'.format(json['id'], json['name']))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')

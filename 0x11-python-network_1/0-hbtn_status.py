#!/usr/bin/python3
"""a module that fetches https://alx-intranet.hbtn.io/status using urllib"""

import urllib.request


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
    print('Body response:')
    print('    - type: ', type(body))
    print('    - content: ', body)
    print('    - utf-8 content: ', body.decode())

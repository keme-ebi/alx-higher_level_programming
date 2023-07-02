#!/bin/bash
# sends GET request and displays the body of the response using header variable
curl -s -H 'X-School-User-Id: 98' "$1"

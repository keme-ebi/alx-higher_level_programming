#!/bin/bash
# writes a request to the url and displays the size in bytes
curl -sI "$1" | awk '/Content-Length/ {print $2}' | tr -d '\r'

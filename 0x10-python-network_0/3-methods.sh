#!/bin/bash
# displays all http methods allowed by the server
curl -sI "$1" | awk -F': ' '/^Allow/ {print substr($2, 1, length($2)-1)}'

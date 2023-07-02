#!/bin/bash
# sends a POST request from a json file
curl -s -X POST -d @"$2" -H "Content-Type: application/json" "$1"

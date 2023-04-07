#!/bin/bash
# a bash script that print the response code from http request
curl -so /dev/null -w "%{http_code}" "$1"

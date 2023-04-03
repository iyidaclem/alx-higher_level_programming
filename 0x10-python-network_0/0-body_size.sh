#!/usr/bin/bash
# get Content-Length of a request
curl -sI $1 | grep "Content-Length" | sed 's/Content-Length: //'


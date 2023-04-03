#!/bin/bash
# get Content-Length of a request
curl -s $1 | wc -c

#!/bin/bash
# A bash script to sent json post request and display body of the response
curl -s $1 -d @2 -X POST -H "Content-Type: Application/json"

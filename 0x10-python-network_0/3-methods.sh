#!/bin/bash
# Display all the allowd HTTP method
curl -v $1 | grep 'Allow' | cut -d " " -f 2-

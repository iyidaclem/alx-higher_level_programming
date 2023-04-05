#!/bin/bash
# Display all the allowd HTTP method
curl -sI -X OPTIONS $1 | grep 'Allow:' | cut -d " " -f 2-

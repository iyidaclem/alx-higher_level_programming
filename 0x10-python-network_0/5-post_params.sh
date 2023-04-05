#!/bin/bash
# Send post request through curl
curl -s $1 -X POST -d "email=test@gmail&subject=I will always be here for PLD"

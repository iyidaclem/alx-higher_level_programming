#!/bin/bash
# Send post request through curl
curl -sL -X POST -d "email=test@gmail" -d "subject=I will always be here for PLD"  $1

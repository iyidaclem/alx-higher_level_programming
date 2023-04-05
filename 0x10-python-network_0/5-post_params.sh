#!/bin/bash
# Send post request through curl
curl -sL -d "email: test@email" -d "subject: I will always be here for PLD"  $1

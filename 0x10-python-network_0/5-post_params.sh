#!/bin/bash
#sends POST request to the URL and displays body of the response
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"

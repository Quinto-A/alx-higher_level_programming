#!/bin/bash
#takes in URL and displays all HTTPS methods server will allow
curl -sI -X OPTIONS "$1" | grep -i "^Allow:" | cut -d' ' -f2-

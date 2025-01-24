#!/bin/bash
#Sends request to URL and displays only the status code of the reply
curl -s -o /dev/null -w "%{http_code}" "$1"

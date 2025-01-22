#!/bin/bash
#sends GET request and displays only body of code 200
curl -s -w "%{http_code}%" "$1" -o response_body | grep -q "^200$" && cat response_body

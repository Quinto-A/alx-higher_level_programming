#!/bin/bash
#sends GET request and displays only body of code 200
[ "$(curl -sL -w "%{http_code}%" -o response_body "$1")" eq 200 ] && cat response_body || echo "Request failed"

#!/bin/bash
#sends GET request and displays only body of code 200
status=$(curl -sL -w "%{http_code}" -o response_body "$1"); [ "$status" = "200" ] && cat response_body || echo "Request failed"

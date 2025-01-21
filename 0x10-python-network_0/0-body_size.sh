#!/bin/bash

if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

URL="$1"

BODY_SIZE=$(curl -s -o /dev/null -w '%{size_download}' "$URL")

echo "The size of the body of the response is ${BODY_SIZE} bytes"

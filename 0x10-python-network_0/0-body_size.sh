#!/bin/bash
#check if URL provided
curl -s -o /dev/null -w '%{size_download}\n' "$1"

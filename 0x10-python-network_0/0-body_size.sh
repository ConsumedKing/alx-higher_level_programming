#!/usr/bin/env bash
#this script is used to send an http request to a target IP:PORT
response_headers=$(curl -s -I "$1")
echo "$response_headers" | grep -i 'Content-Length' | cut -d ':' -f2

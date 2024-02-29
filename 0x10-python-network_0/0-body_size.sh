#!/usr/bin/env bash
#this script is used to send an http request to a target IP:PORT
curl -s "$1" | wc -c

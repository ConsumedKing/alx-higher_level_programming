#!/bin/bash
#my life is gone officialy
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-

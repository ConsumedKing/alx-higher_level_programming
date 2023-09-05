#!/usr/bin/python3
for i in "abcdefghijklmnopqrstuvwxyz":
    if i == 'e' or i == 'q':
        continue
    print("{0}".format(i), end="")

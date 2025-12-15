#!/bin/python

import sys

if len(sys.argv) > 2:
    print("usage: nl.py filename")
    sys.exit(0)

inp = sys.stdin
if (len(sys.argv) == 2):
    inp = open(sys.argv[1], "r")

cnt = 1
for line in inp:
    line = line.rstrip("\n")
    print("{}: {}".format(cnt, line))
    cnt += 1

inp.close()

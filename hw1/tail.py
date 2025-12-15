#!/bin/python

import sys
from collections import deque

def tail(inp, l = 10, filename = ""):
    if filename != "":
        print("==> {} <==".format(filename))
    last = deque(inp, maxlen=l)
    for line in last:
        line = line.rstrip("\n")
        print(line)

if (len(sys.argv) == 1):
    tail(sys.stdin, 17)
    sys.exit(0)

if (len(sys.argv) == 2):
    inp = open(sys.argv[1], "r")
    tail(inp)
    inp.close()
    sys.exit(0)

for file in sys.argv[1:]:
    inp = open(file, "r")
    tail(inp, filename=file)
    inp.close()

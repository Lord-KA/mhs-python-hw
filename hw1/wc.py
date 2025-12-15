#!/bin/python

import sys

def wc(inp):
    lines = 0
    words = 0
    chars = 0
    for line in inp:
        lines += 1
        words += len(line.split())
        chars += len(line)
    return lines, words, chars

if len(sys.argv) == 1:
    l, w, c = wc(sys.stdin)
    print(f"{l:4d}{w:4d}{c:4d}")
    sys.exit(0)

total_l = 0
total_w = 0
total_c = 0

for file in sys.argv[1:]:
    inp = open(file, 'r')

    l, w, c = wc(inp)
    total_l += l
    total_w += w
    total_c += c

    inp.close()
    print(f"{l:4d}{w:4d}{c:4d} {file}")

if len(sys.argv) > 2:
    print(f"{total_l:4d}{total_w:4d}{total_c:4d} total")

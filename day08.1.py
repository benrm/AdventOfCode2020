#!/usr/bin/python

import argparse
import re
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

r = re.compile("(\w+) ([+-]\d+)")
program = [ r.match(x).groups() for x in args.input.readlines() ]
visited = set()
acc = 0
idx = 0

while True:
    line = program[idx]
    if idx in visited:
        break
    visited.add(idx)
    if line[0] == "acc":
        acc += int(line[1])
        idx += 1
    elif line[0] == "jmp":
        idx += int(line[1])
    elif line[0] == "nop":
        idx += 1

print("Accumulator: " + str(acc))

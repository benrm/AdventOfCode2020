#!/usr/bin/python

import argparse
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

lines = sorted([ int(x) for x in args.input.readlines() ])
lines.insert(0, 0)
lines.append(lines[len(lines)-1]+3)

neighbors = dict()

for i in range(len(lines)):
    neighbors[lines[i]] = set()
    j = i+1
    while j < len(lines) and lines[j] <= lines[i]+3:
        neighbors[lines[i]].add(lines[j])
        j += 1

combinations = dict()

def cmb(adapters):
    if len(adapters) == 1:
        return 1
    sum_ = 0
    for n in neighbors[adapters[0]]:
        if n in combinations:
            sum_ += combinations[n]
        else:
            i = adapters.index(n)
            combinations[n] = cmb(adapters[i:])
            sum_ += combinations[n]
    return sum_

print(str(cmb(lines)))

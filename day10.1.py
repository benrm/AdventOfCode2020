#!/usr/bin/python

import argparse
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

lines = sorted([ int(x) for x in args.input.readlines() ])

diffs = { 1: 0, 2: 0, 3: 1 }

diffs[lines[0]] += 1
for idx in range(len(lines)-1):
    diffs[lines[idx+1]-lines[idx]] += 1

print("Value: " + str(diffs[1] * diffs[3]))

#!/usr/bin/python

import argparse
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

lines = [ int(x) for x in args.input.readlines() ]

for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        sum = lines[i] + lines[j]
        if sum == 2020:
            print(str(lines[i] * lines[j]))
            exit(0)

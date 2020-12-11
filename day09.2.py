#!/usr/bin/python

import argparse
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
parser.add_argument("-s", "--sum", type=int, default=85848519)
args = parser.parse_args()

lines = [ int(x) for x in args.input.readlines() ]

for i in range(len(lines)):
    sum_ = lines[i]
    min_ = lines[i]
    max_ = lines[i]
    for j in range(i+1, len(lines)):
        if lines[j] < min_:
            min_ = lines[j]
        if lines[j] > max_:
            max_ = lines[j]
        sum_ += lines[j]
        if sum_ == args.sum:
            print("Value: " + str(min_+max_))
            exit(0)

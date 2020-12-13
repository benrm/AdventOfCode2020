#!/usr/bin/python

import argparse
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

start = int(args.input.readline())
buses = [ int(x) for x in args.input.readline().split(",") if x != "x" ]

min_ = None
bus = None
for b in buses:
    mod = start % b
    if mod == 0:
        min_ = start
        bus = b
    etd = start + b - mod
    if min_ == None or etd < min_:
        min_ = etd
        bus = b

print(str((min_-start)*bus))

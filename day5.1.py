#!/usr/bin/python

import argparse
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

lines = [ x.strip() for x in args.input.readlines() ]

max_id = 0
for line in lines:
    min_ = 0
    max_ = 127
    len_ = 128
    for idx in range(0,7):
        len_ = int(len_/2)
        if line[idx] == "F":
            max_ = min_ + len_ - 1
        elif line[idx] == "B":
            min_ = min_ + len_
    row = min_
    min_ = 0
    max_ = 7
    len_ = 8
    for idx in range(7, 10):
        len_ = int(len_/2)
        if line[idx] == "L":
            max_ = min_ + len_ - 1
        elif line[idx] == "R":
            min_ = min_ + len_
    column = min_
    id_ = row * 8 + column
    if id_ > max_id:
        max_id = id_
print("Max:" + str(max_id))

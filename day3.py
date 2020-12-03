#!/usr/bin/python

import argparse
import math
import string
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

x = 0
y = 0

trees = set()

lines = [ x.strip() for x in args.input.readlines() ]

width = len(lines[0])
height = len(lines)

for line in lines:
    x = 0
    for char in line:
        if char == "#":
            trees.add((x,y))
        x += 1
    y += 1

x = 0
y = 0

count = 0
while y < height:
    if (x, y) in trees:
        count +=1
    x = (x + 3) % width
    y += 1

print("Trees: " + str(count))

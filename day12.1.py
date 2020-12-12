#!/usr/bin/python

import argparse
import math
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

directions = [ (line[0], int(line[1:])) for line in args.input.readlines() ]

angle = 0
pos = (0,0)
for d in directions:
    if d[0] == "N":
        pos = (pos[0], pos[1]+d[1])
    elif d[0] == "E":
        pos = (pos[0]+d[1], pos[1])
    elif d[0] == "S":
        pos = (pos[0], pos[1]-d[1])
    elif d[0] == "W":
        pos = (pos[0]-d[1], pos[1])
    elif d[0] == "L":
        angle += math.radians(d[1])
    elif d[0] == "R":
        angle -= math.radians(d[1])
    elif d[0] == "F":
        x = pos[0] + math.cos(angle)*d[1]
        y = pos[1] + math.sin(angle)*d[1]
        pos = (x, y)

print("Value: "+str(int(abs(pos[0])+abs(pos[1]))))

#!/usr/bin/python

import argparse
import math
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

directions = [ (line[0], int(line[1:])) for line in args.input.readlines() ]

(px, py) = (0,0)
(wx, wy) = (10,1)
for d in directions:
    if d[0] == "N":
        wy += d[1]
    elif d[0] == "E":
        wx += d[1]
    elif d[0] == "S":
        wy -= d[1]
    elif d[0] == "W":
        wx -= d[1]
    elif d[0] == "L" or d[0] == "R" or d[0] == "F":
        l = math.dist((px,py),(wx,wy)) 
        angle = math.atan2(wy-py,wx-px)
        if d[0] == "L":
            angle += math.radians(d[1])
            wx = px + math.cos(angle)*l
            wy = py + math.sin(angle)*l
        elif d[0] == "R":
            angle -= math.radians(d[1])
            wx = px + math.cos(angle)*l
            wy = py + math.sin(angle)*l
        elif d[0] == "F":
            px += l*math.cos(angle)*d[1]
            py += l*math.sin(angle)*d[1]
            wx += l*math.cos(angle)*d[1]
            wy += l*math.sin(angle)*d[1]

print("Value: "+str(int(abs(px)+abs(py))))

#!/usr/bin/python

import argparse
import re
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

groups = [ x.split() for x in args.input.read().split("\n\n") ]

total = 0
for group in groups:
    yeses = list()
    for line in group:
        yes = set()
        for char in line:
            if char not in yes:
                yes.add(char)
        yeses.append(yes)
    intersection = yeses[0]
    if len(yeses) > 1:
        for yes in yeses[1:len(yeses)]:
            intersection = intersection.intersection(yes)
    total += len(intersection)

print("Total: " + str(total))

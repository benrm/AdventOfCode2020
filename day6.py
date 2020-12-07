#!/usr/bin/python

import argparse
import re
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

p = re.compile("\s+")
groups = [ re.sub(p, "", x) for x in args.input.read().split("\n\n") ]

total = 0
for group in groups:
    yes = set()
    for char in group:
        if char not in yes:
            yes.add(char)
    total += len(yes)

print("Yes: " + str(total))

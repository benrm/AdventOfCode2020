#!/usr/bin/python

import argparse
import re
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

reg = re.compile("(\d+)-(\d+)\s+(.):\s+(.*)")

lines = args.input.readlines()

valid = 0
invalid = 1

for line in lines:
    match = reg.match(line)
    if match:
        c_min = int(match[1])
        c_max = int(match[2])
        char = match[3]
        string = match[4]
        count = string.count(char)
        if count >= c_min and count <= c_max:
            valid += 1
        else:
            invalid += 1

print("Valid: " + str(valid))
print("Invalid: " + str(invalid))

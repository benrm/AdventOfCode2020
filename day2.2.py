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
        idx1 = int(match[1]) - 1
        idx2 = int(match[2]) - 1
        char = match[3]
        string = match[4]
        if (idx1 < len(string) and string[idx1] == char) ^ (idx2 < len(string) and string[idx2] == char):
            valid += 1
        else:
            invalid += 1

print("Valid: " + str(valid))
print("Invalid: " + str(invalid))

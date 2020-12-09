#!/usr/bin/python

import argparse
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

lines = args.input.readlines()

for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        for k in range(j+1, len(lines)):
            sum = int(lines[i]) + int(lines[j]) + int(lines[k])
            if sum == 2020:
                print(str(int(lines[i]) * int(lines[j]) * int(lines[k])))
                exit(0)

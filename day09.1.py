#!/usr/bin/python

import argparse
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

lines = [ int(x) for x in args.input.readlines() ]

for i in range(len(lines)):
    if i > 25:
        valid = False
        for j in range(i-25,i):
            for k in range(j+1,i):
                if j == k:
                    continue
                if lines[j] + lines[k] == lines[i]:
                    valid = True
                    break
            if valid == True:
                break
        if valid == False:
            print("Line " + str(i) + " (" + str(lines[i]) + ") is invalid")
            break

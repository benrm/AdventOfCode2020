#!/usr/bin/python

import argparse
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
parser.add_argument("-n", "--number", type=int)
args = parser.parse_args()

numbers = [ int(x) for x in args.input.read().split(",") ]

history = dict()

for idx in range(len(numbers)-1):
    history[numbers[idx]] = idx+1

for i in range(len(numbers),args.number):
    n = numbers[i-1]
    if n not in history:
        numbers.append(0)
        history[n] = i
    else:
        numbers.append(i-history[n])
        history[n] = i

print(numbers[args.number-1])

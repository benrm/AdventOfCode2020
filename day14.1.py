#!/usr/bin/python

import argparse
import re
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

onemask = 0
zeromask = 0

memory = dict()

maskre = re.compile("mask = ([01X]{36})")
memre = re.compile("mem\[(\d+)\] = (\d+)")

lines = [ x.strip() for x in args.input.readlines() ]

for line in lines:
    match = memre.match(line)
    if match:
        memory[int(match[1])] = ~(~(int(match[2])|onemask)|zeromask)
    else:
        match = maskre.match(line)

        onemask = 0
        zeromask = 0

        for bit in match[1]:
            onemask = onemask << 1
            zeromask = zeromask << 1

            if bit == "1":
                onemask = onemask | 1
            elif bit == "0":
                zeromask = zeromask | 1

print("Value: "+str(sum(memory.values())))

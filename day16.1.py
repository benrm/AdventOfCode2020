#!/usr/bin/python

import argparse
import re
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
parser.add_argument("-n", "--number", type=int)
args = parser.parse_args()

rules = list()
rulere = re.compile("([^:]+): (\d+)-(\d+) or (\d+)-(\d+)")
while True:
    line = args.input.readline()
    if line == "\n":
        break
    match = rulere.match(line)
    if match == None:
        print("Parse error")
        exit(1)
    rules.append((int(match[2]),int(match[3])))
    rules.append((int(match[4]),int(match[5])))

args.input.readline() # "your ticket:"
my_ticket = [ int(x) for x in args.input.readline().split(",") ]

args.input.readline() # "\n"
args.input.readline() # "nearby tickets:"

tickets = [ [ int(x) for x in line.split(",") ] for line in args.input.readlines() ]

error_rate = 0
for ticket in tickets:
    for field in ticket:
        is_valid = False
        for rule in rules:
            if rule[0] <= field and field <= rule[1]:
                is_valid = True
                break
        if is_valid == False:
            error_rate += field

print("Value: "+str(error_rate))

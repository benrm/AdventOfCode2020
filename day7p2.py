#!/usr/bin/python

import argparse
import re
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

lines = [ x.strip() for x in args.input.readlines() ]

rules = dict()
key = re.compile("(\w+ \w+) bags? contain")
bags = re.compile("(\d+) (\w+ \w+) bags?")
for line in lines:
    km = key.match(line)
    bms = bags.findall(line[km.end():len(line)])
    if km[1] not in rules:
        rule = set()
        for bm in bms:
            rule.add((bm[1], int(bm[0])))
        rules[km[1]] = rule

def total_bags(color):
    total = 0
    for bag in rules[color]:
        subtotal = total_bags(bag[0])
        if subtotal != None:
            total += total_bags(bag[0]) * bag[1] + bag[1]
    return total

print("Total: " + str(total_bags("shiny gold")))

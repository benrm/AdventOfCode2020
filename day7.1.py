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
            rule.add((bm[1], bm[0]))
        rules[km[1]] = rule

total = 0
for key in rules:
    visited = set(key)
    queue = [ x[0] for x in rules[key] ]
    print("Queue: " + str(queue))
    while len(queue) > 0:
        visit = queue.pop(0)
        if visit not in visited:
            visited.add(visit)
            if visit == "shiny gold":
                total += 1
                break
            for neighbor in rules[visit]:
                queue.append(neighbor[0])

print("Rules: " + str(total))

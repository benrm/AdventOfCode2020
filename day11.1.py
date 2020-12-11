#!/usr/bin/python

import argparse
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

seats = dict()

x = 0
y = 0

for char in args.input.read():
    if char == "L":
        seats[(x, y)] = set()
        x += 1
    elif char == ".":
        x += 1
    elif char == "\n":
        x = 0
        y += 1

for seat in seats:
    for x in [seat[0]-1,seat[0],seat[0]+1]:
        for y in [seat[1]-1,seat[1],seat[1]+1]:
            if (x, y) == seat:
                continue
            if (x, y) in seats:
                seats[seat].add((x, y))

occupied = set()
vacate = set()
visit = set()

while True:
    for seat in seats:
        count = 0
        for neighbor in seats[seat]:
            if neighbor in occupied:
                count += 1
        if count == 0 and seat not in occupied:
            visit.add(seat)
        elif count >= 4 and seat in occupied:
            vacate.add(seat)
    if len(vacate) == 0 and len(visit) == 0:
        break
    occupied = (occupied - vacate) | visit
    vacate = set()
    visit = set()

print("Value: " + str(len(occupied)))

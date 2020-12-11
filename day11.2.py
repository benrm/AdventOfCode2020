#!/usr/bin/python

import argparse
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

seats = dict()

x = 0
y = 0

width = 0

for char in args.input.read():
    if char == "L":
        seats[(x, y)] = set()
        x += 1
    elif char == ".":
        x += 1
    elif char == "\n":
        width = x
        x = 0
        y += 1

height = y

for seat in seats:
    for dir_ in [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]:
        x = seat[0]
        y = seat[1]
        while x >= 0 and x <= width and y >= 0 and y <= height:
            x += dir_[0]
            y += dir_[1]
            if (x, y) in seats:
                seats[seat].add((x, y))
                break

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
        elif count >= 5 and seat in occupied:
            vacate.add(seat)
    if len(vacate) == 0 and len(visit) == 0:
        break
    occupied = (occupied - vacate) | visit
    vacate = set()
    visit = set()

print("Value: " + str(len(occupied)))

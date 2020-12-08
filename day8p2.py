#!/usr/bin/python

import argparse
import re
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

r = re.compile("(\w+) ([+-]\d+)")
program = [ r.match(x).groups() for x in args.input.readlines() ]
for fixup in range(len(program)):
    p = program.copy()
    if program[fixup][0] == "jmp":
        p[fixup] = ("nop", int(program[fixup][1]))
    elif program[fixup][0] == "nop" and fixup + int(program[fixup][1]) == len(program):
        p[fixup] = ("jmp", int(program[fixup][1]))
    else:
        continue

    finish = False
    visited = set()
    acc = 0
    idx = 0
    while True:
        if idx in visited:
            break
        visited.add(idx)
        if idx == len(p):
            finish = True
            break
        line = p[idx]
        if line[0] == "acc":
            acc += int(line[1])
            idx += 1
        elif line[0] == "jmp":
            idx += int(line[1])
        elif line[0] == "nop":
            idx += 1
    if finish:
        print("Accumulated: " + str(acc))

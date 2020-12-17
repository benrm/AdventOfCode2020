#!/usr/bin/python

import argparse
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

cubes = set()
active = set()

x = 0
y = 0
for char in args.input.read():
    if char == ".":
        x += 1
    elif char == "#":
        active.add((x,y,0,0))
        for i in [x-1,x,x+1]:
            for j in [y-1,y,y+1]:
                for k in [-1,0,1]:
                    for l in [-1,0,1]:
                        cubes.add((i,j,k,l))
        x += 1
    elif char == "\n":
        x = 0
        y += 1

deactivate = set()
activate = set()

to_add = set()

for a in range(6):
    for cube in cubes:
        (x, y, z, q) = cube
        neighbors = 0
        for i in [x-1,x,x+1]:
            for j in [y-1,y,y+1]:
                for k in [z-1,z,z+1]:
                    for l in [q-1,q,q+1]:
                        if (i,j,k,l) == cube:
                            continue
                        if (i,j,k,l) in active:
                            neighbors += 1
                        to_add.add((i,j,k,l))

        if cube in active and neighbors != 2 and neighbors != 3:
            deactivate.add(cube)
        elif neighbors == 3 and cube not in active:
            activate.add(cube)

    cubes |= to_add
    to_add.clear()

    active |= activate
    activate.clear()

    active -= deactivate
    deactivate.clear()

print("Value: "+str(len(active)))

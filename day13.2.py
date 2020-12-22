#!/usr/bin/python

import argparse
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

args.input.readline() # Ignore
arr = args.input.readline().split(",")

buses = list()
for idx in range(len(arr)):
    if arr[idx] != "x":
        if idx != 0:
            buses.append((int(arr[idx]), int(arr[idx]) - idx))
        else:
            start = int(arr[idx])

def inverse(a, n):
    t = 0
    newt = 1
    r = n
    newr = a

    while newr != 0:
        quotient = r // newr
        (t, newt) = (newt, t-quotient*newt)
        (r, newr) = (newr, r-quotient*newr)

    if r > 1:
        return None
    if t < 0:
        t += n

    return t

M = 1
for bus in buses:
    M *= bus[0]

moduli = [ M // bus[0] for bus in buses ]

inverses = list()
for idx in range(len(buses)):
    inverses.append(inverse(moduli[idx], buses[idx][0]))

sum_ = 0
for idx in range(len(buses)):
    sum_ += buses[idx][1]*moduli[idx]*inverses[idx]

val = sum_ % M

while val % start != 0:
    val += M

print("Value: "+str(val))

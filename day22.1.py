#!/usr/bin/python

import argparse
import re
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

numre = re.compile(r"\d+")
halves = args.input.read().split("\n\n")
deck1 = [ int(x) for x in halves[0].split("\n")[1:] if numre.match(x) ]
deck2 = [ int(x) for x in halves[1].split("\n")[1:] if numre.match(x) ]

while len(deck1) > 0 and len(deck2) > 0:
    card1 = deck1.pop(0)
    card2 = deck2.pop(0)

    if card1 > card2:
        deck1.append(card1)
        deck1.append(card2)
    else:
        deck2.append(card2)
        deck2.append(card1)

winner = deck1 if len(deck1) > 0 else deck2

sum_ = 0
for idx in range(len(winner)):
    sum_ += winner[idx]*(len(winner)-idx)

print("Value: "+str(sum_))

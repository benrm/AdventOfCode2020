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

def decksum(deck):
    sum_ = 0
    for idx in range(len(deck)):
        sum_ += deck[idx]*(len(deck)-idx)
    return sum_

def play(deck1, deck2):
    played = set()

    while len(deck1) > 0 and len(deck2) > 0:
        sums = (decksum(deck1), decksum(deck2))
        if sums in played:
            break
        played.add(sums)

        card1 = deck1.pop(0)
        card2 = deck2.pop(0)

        if len(deck1) >= card1 and len(deck2) >= card2:
            newdeck1 = deck1.copy()[:card1]
            newdeck2 = deck2.copy()[:card2]
            winner = play(newdeck1, newdeck2)
        else:
            winner = card1 > card2

        if winner:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)

    return len(deck1) > 0

winner = deck1 if play(deck1, deck2) else deck2

print("Value: "+str(decksum(winner)))

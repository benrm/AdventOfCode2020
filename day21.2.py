#!/usr/bin/python

import argparse
import re
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

recipere = re.compile(r'((?:\w+ )+)\(contains (\w+(?:, \w+)*)\)')
wordre = re.compile(r'\w+')
allergen_dict = {}
for recipe in args.input.readlines():
    match = recipere.match(recipe)
    if match:
        ingredients = set(wordre.findall(match[1]))
        allergens = set(wordre.findall(match[2]))

        for allergen in allergens:
            if allergen not in allergen_dict:
                allergen_dict[allergen] = ingredients
            else:
                allergen_dict[allergen] = allergen_dict[allergen] & ingredients

arr = list()
for allergen in allergen_dict:
    arr.append((allergen, len(allergen_dict[allergen])))

arr.sort(key=lambda x : x[1])
allergens = [ x[0] for x in arr ]

used = set()

def search(allergens, used):
    if len(allergens) > 0:
        allergen = allergens.pop(0)
        for food in allergen_dict[allergen]:
            if food not in used:
                used.add(food)
                ret = search(allergens, used)
                if ret != None:
                    ret[allergen] = food
                    return ret
                else:
                    used.remove(food)
        allergens.insert(0,allergen)
        return None
    else:
        return {}

ret = search(allergens, used)

print("Solution: "+",".join([ x[1] for x in sorted([ (y, ret[y]) for y in ret ]) ]))

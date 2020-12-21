#!/usr/bin/python

import argparse
import re
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

recipere = re.compile(r'((?:\w+ )+)\(contains (\w+(?:, \w+)*)\)')
wordre = re.compile(r'\w+')
counts = {}
allergen_dict = {}
all_ingredients = set()
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

        all_ingredients |= ingredients

        for ingredient in ingredients:
            if ingredient not in counts:
                counts[ingredient] = 1
            else:
                counts[ingredient] += 1

allergens = set()
for allergen in allergen_dict.values():
    allergens |= allergen

not_allergens = all_ingredients - allergens

sum_ = 0
for ingredient in not_allergens:
    sum_ += counts[ingredient]

print("Value: "+str(sum_))

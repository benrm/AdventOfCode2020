#!/usr/bin/python

import argparse
import re
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

ids = args.input.read().split("\n\n")

fields_required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

valid = 0

field_re = re.compile("([\w]+):([#\w]+)")

for id_ in ids:
    fields_present = set()
    matches = field_re.findall(id_)
    for match in matches:
        fields_present.add(match[0])
    if fields_required <= fields_present:
        valid += 1

print("Valid: " + str(valid))

#!/usr/bin/python

import argparse
import re
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
args = parser.parse_args()

ids = args.input.read().split("\n\n")

year_re = re.compile("^\d{4}$")
def validate_year(min_, max_):
    def ret(year):
        if year_re.match(year) == None:
            return False
        return int(year) >= min_ and int(year) <= max_
    return ret

height_re = re.compile("^(\d+)(cm|in)$")
def validate_height(height):
    match = height_re.match(height)
    if match == None:
        return False
    elif match[2] == "cm":
        return int(match[1]) >= 150 and int(match[1]) <= 193
    else:
        return int(match[1]) >= 59 and int(match[1]) <= 76

hair_re = re.compile("^#[\da-f]{6}$")
def validate_hair(hair):
    return hair_re.match(hair) != None

def validate_eye(eye):
    return eye in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

pid_re = re.compile("^\d{9}$")
def validate_pid(pid):
    return pid_re.match(pid) != None

fields_required = {
        "byr": validate_year(1920, 2002),
        "iyr": validate_year(2010, 2020),
        "eyr": validate_year(2020, 2030),
        "hgt": validate_height,
        "hcl": validate_hair,
        "ecl": validate_eye,
        "pid": validate_pid,
        }

valid = 0

field_re = re.compile("([\w]+):([#\w]+)")

for id_ in ids:
    fields_present = set()
    matches = field_re.findall(id_)
    for match in matches:
        if match[0] in fields_required.keys():
            if fields_required[match[0]](match[1]):
                fields_present.add(match[0])
            else:
                break

    if fields_required.keys() <= fields_present:
        valid += 1

print("Valid: " + str(valid))

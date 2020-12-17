#!/usr/bin/python

import argparse
import re
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
parser.add_argument("-n", "--number", type=int)
args = parser.parse_args()

rules = dict()
rulere = re.compile("([^:]+): (\d+)-(\d+) or (\d+)-(\d+)")
while True:
    line = args.input.readline()
    if line == "\n":
        break
    match = rulere.match(line)
    if match == None:
        print("Parse error")
        exit(1)
    rules[match[1]] = [(int(match[2]),int(match[3])),(int(match[4]),int(match[5]))]

args.input.readline() # "your ticket:"
my_ticket = [ int(x) for x in args.input.readline().split(",") ]

args.input.readline() # "\n"
args.input.readline() # "nearby tickets:"

tickets = [ [ int(x) for x in line.split(",") ] for line in args.input.readlines() ]

valid_tickets = list()

for ticket in tickets:
    is_ticket_valid = True
    for field in ticket:
        is_field_valid = False
        for rule in rules:
            if (rules[rule][0][0] <= field and rules[rule][0][1] >= field) or (rules[rule][1][0] <= field and rules[rule][1][1] >= field):
                is_field_valid = True
        if is_field_valid == False:
            is_ticket_valid = False
    if is_ticket_valid == True:
        valid_tickets.append(ticket)

fields = list()

for rule in rules:
    valid = set()
    for idx in range(len(my_ticket)):
        is_valid = True
        for ticket in valid_tickets:
            if (rules[rule][0][0] > ticket[idx] or rules[rule][0][1] < ticket[idx]) and (rules[rule][1][0] > ticket[idx] or rules[rule][1][1] < ticket[idx]):
                is_valid = False
        if is_valid:
            valid.add(idx)
    fields.append((rule, valid))

fields.sort(key=lambda x: len(x[1]))

def search(fields, available):
    (field, indices) = fields.pop(0)
    for idx in indices:
        if idx in available:
            if len(fields) == 0:
                return { field: idx }

            fields_copy = fields.copy()
            avail_copy = available.copy()
            avail_copy.remove(idx)

            ret = search(fields_copy, avail_copy)

            if ret != None:
                ret[field] = idx
                return ret
    return None

keymap = search(fields, set(range(len(my_ticket))))

product = 1
depre = re.compile("^departure")
for key in keymap:
    if depre.match(key):
        product *= my_ticket[keymap[key]]

print("Value: "+str(product))

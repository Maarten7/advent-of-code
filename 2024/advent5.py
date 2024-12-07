import numpy as np
import os
import re
from pathlib import Path

from math import floor
from functools import cmp_to_key

def make_rule_dict(ordering_rules):
    rule_dict = {}
    reverse_rule_dict = {}
    for key, value in ordering_rules:
        rule_dict.setdefault(key, []).append(value)
    for key, value in ordering_rules:
        reverse_rule_dict.setdefault(value, []).append(key)
    return rule_dict, reverse_rule_dict

def in_order(line, reversed_rule_dict):
    if len(line) == 1:
        return True

    first_element = line[0]
    rests = line[1:]

    try:
        cant_come_after = reversed_rule_dict[first_element]
    except KeyError:
        return in_order(rests, reversed_rule_dict)

    if any([rest in cant_come_after for rest in rests]):
        return False
    else:
        return in_order(rests, reversed_rule_dict)


def main_1(file):
    # input = np.loadtxt(file, dtype=int)
    input = open(file, "r").read()
    input = input.split()
    ordering_rules = [
        list(map(int, line.split("|"))) for line in input if len(line) == 5
    ]
    to_be_updated = [list(map(int, line.split(","))) for line in input if len(line) > 5]
    rule_dict, reversed_rule_dict = make_rule_dict(ordering_rules)
    return sum(
        map(
            lambda line: line[floor(len(line) / 2)],
            filter(lambda line: in_order(line, reversed_rule_dict), to_be_updated),
        )
    )


def main_2(file):
    input = open(file, "r").read()
    input = input.split()
    ordering_rules = [
        list(map(int, line.split("|"))) for line in input if len(line) == 5
    ]
    to_be_updated = [list(map(int, line.split(","))) for line in input if len(line) > 5]

    rule_dict, reversed_rule_dict = make_rule_dict(ordering_rules)

    def compare(el1, el2):
        if el2 in rule_dict.get(el1, []):
            return 1
        if el1 in rule_dict.get(el2, []):
            return -1
        else:
            return 0

    return sum(
        map(
            lambda line: line[floor(len(line) / 2)],
            map(
                lambda x: sorted(x, key=cmp_to_key(compare)),
                filter(
                    lambda line: not in_order(line, reversed_rule_dict), to_be_updated
                ),
            ),
        )
    )


if __name__ == "__main__":
    advent_day = Path(os.path.basename(__file__)).stem

    file = f"test_input_{advent_day}.txt"
    test_1 = main_1(file)
    print(test_1)
    if test_1 == 143:
        file = f"input_{advent_day}.txt"
        print(main_1(file))

    file = f"test_input_{advent_day}.txt"
    test_2 = main_2(file)
    print(test_2)
    if test_2:
        file = f"input_{advent_day}.txt"
        print(main_2(file))

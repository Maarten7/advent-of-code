import numpy as np
import os
from pathlib import Path

import re


def main_1(array):
    muls = re.findall(r"mul\(\d+,\d+\)", array)

    get_digits = lambda mul: re.findall(r"\d+", mul)
    digits = map(get_digits, muls)

    to_int = lambda a: int(a[0]) * int(a[1])
    return sum(map(to_int, digits))


def main_2(array):
    print(array)
    muls = np.array(re.findall(r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)", array))

    get_digits = lambda mul: re.findall(r"\d+", mul)
    to_int = lambda a: int(a[0]) * int(a[1])

    total = 0
    active = True
    for mul in muls:
        if mul == "don't()":
            active = False
            continue

        if mul == "do()":
            active = True
            continue

        if active:
            total += to_int(get_digits(mul))

    return total


if __name__ == "__main__":
    advent_day = Path(os.path.basename(__file__)).stem

    file = f"test_input_{advent_day}.txt"
    # input = np.loadtxt(file, dtype=int)
    input = open(file, "r").read()
    test_1 = main_1(input)
    print(test_1)
    if test_1 == 162:
        file = f"input_{advent_day}.txt"
        input = open(file, "r").read()
        # print(main_1(input))

    test_2 = main_2(
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    )
    print(test_2)
    if test_2 == 48:
        file = f"input_{advent_day}.txt"
        input = open(file, "r").read()
        print(main_2(input))

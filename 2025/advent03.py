import numpy as np
import os
import re
import math
from pathlib import Path
import itertools


def get_max_two(el):
    m1 = max(el)
    i = el.index(m1)
    el[i] = -1
    m2 = max(el)
    el[i] = m1

    j = el.index(m2)

    if i < j:
        x = int(str(m1) + str(m2))
    else:
        z = int(str(m2) + str(m1))
        if el[i + 1 :]:
            y = int(str(m1) + str(max(el[i + 1 :])))
            x = max(z, y)
        else:
            x = z
    return x


def get_max_twolf(el, n=12, outnumber=""):
    if n == 1:
        return int(outnumber + str(max(el)))

    mm = max(el[: -n + 1])
    i = el.index(mm)

    return get_max_twolf(el[i + 1 :], n - 1, outnumber=outnumber + str(mm))


def main_1(file):
    input = np.loadtxt(file, dtype=str)
    input = [[int(z) for z in list(el)] for el in input]

    score = 0
    for i, el in enumerate(input):
        score += get_max_two(el)
    return score


def main_2(file):
    input = np.loadtxt(file, dtype=str)
    input = [[int(z) for z in list(el)] for el in input]

    score = 0
    for el in input:
        score += get_max_twolf(el)

    return score


if __name__ == "__main__":
    TEST_1_ANS = 357
    TEST_2_ANS = 3121910778619
    advent_day = Path(os.path.basename(__file__)).stem
    file = f"input_{advent_day}.txt"
    test_file = f"test_input_{advent_day}.txt"

    test_1 = main_1(test_file)
    print(f"{test_1 = }")
    if test_1 == TEST_1_ANS:
        result_1 = main_1(file)
        print(f"{result_1 = }")

    test_2 = main_2(test_file)
    print(f"{test_2 = }")
    if test_2 == TEST_2_ANS:
        result_2 = main_2(file)
        print(f"{result_2 = }")

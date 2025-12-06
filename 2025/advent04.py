import numpy as np
import os
import re
import math
from pathlib import Path
import itertools


def main_1(file):
    input = np.array([[x for x in list(line)] for line in np.loadtxt(file, dtype=str)])
    a, b = np.where(input == "@")
    ats = set(zip(a, b))
    score = 0
    for i, j in ats:
        neighbors = [
            (i + 1, j + 1),
            (i + 1, j),
            (i + 1, j - 1),
            (i, j + 1),
            (i, j - 1),
            (i - 1, j + 1),
            (i - 1, j),
            (i - 1, j - 1),
        ]

        neighbor_count = 0
        for neighbor in neighbors:
            if neighbor in ats:
                neighbor_count += 1
        if neighbor_count < 4:
            score += 1
    return score


def find_and_remove(ats):
    score = 0
    to_be_removed = []
    for i, j in ats:
        neighbors = [
            (i + 1, j + 1),
            (i + 1, j),
            (i + 1, j - 1),
            (i, j + 1),
            (i, j - 1),
            (i - 1, j + 1),
            (i - 1, j),
            (i - 1, j - 1),
        ]

        neighbor_count = 0
        for neighbor in neighbors:
            if neighbor in ats:
                neighbor_count += 1
        if neighbor_count < 4:
            score += 1
            to_be_removed.append((i, j))

    for remove in to_be_removed:
        ats.remove(remove)
    return ats


def main_2(file):
    input = np.array([[x for x in list(line)] for line in np.loadtxt(file, dtype=str)])
    a, b = np.where(input == "@")
    # change to list here to demonstrate slowness
    ats = set(zip(a, b))

    removed = None
    total = 0
    while removed != 0:
        before = len(ats)
        ats = find_and_remove(ats)
        removed = before - len(ats)
        total += removed
    return total


if __name__ == "__main__":
    TEST_1_ANS = 13
    TEST_2_ANS = 43
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

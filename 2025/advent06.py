import numpy as np
import os
import re
import math
from pathlib import Path
import itertools


def main_1(file):
    input = np.loadtxt(file, dtype=str)
    total_score = 0
    for i in range(len(input[0])):
        opp = input[-1, i]
        numbers = [int(k) for k in input[:-1, i]]
        score = 0 if opp == "+" else 1
        for num in numbers:
            if opp == "*":
                score *= num
            if opp == "+":
                score += num
        total_score += score

    return total_score


def main_2(file):
    input = open(file, "r")
    sheet = []
    for line in input:
        sheet.append(list(line.strip("\n")))

    sheet = np.array(sheet)

    total_score = 0
    for i in range(len(sheet[0])):

        if np.all(sheet[:, i] == " "):
            total_score += score
            continue

        num = int("".join(sheet[:-1, i]))
        opp_place = sheet[-1, i]
        opp = opp_place if opp_place != " " else opp

        if opp_place != " ":
            score = 0 if opp == "+" else 1

        if opp == "*":
            score *= num
        if opp == "+":
            score += num

    return total_score + score


if __name__ == "__main__":
    TEST_1_ANS = 4277556
    TEST_2_ANS = 3263827
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

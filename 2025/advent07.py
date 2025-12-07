import numpy as np
import os
import re
import math
from pathlib import Path
import itertools

def run_tachyon(input):
    for i in range(1, len(input)):
        for j in range(len(input[0])):

            pos = input[i, j]
            above = input[i - 1, j]

            try:
                next = input[i, j + 1]
                diag_forw = input[i - 1, j + 1]
            except IndexError:
                next = "."
                diag_forw = "."
            try:
                prev = input[i, j - 1]
                diag_back = input[i - 1, j - 1]
            except IndexError:
                prev = "."
                diag_back = "."

            if pos == ".":
                if (
                    (above == "S" or above == "|")
                    or (next == "^" and diag_forw == "|")
                    or (prev == "^" and diag_back == "|")
                ):
                    input[i, j] = "|"
    return input

def run_int_tachyon(input):
    for i in range(1, len(input)):
        for j in range(len(input[0])):

            pos = input[i, j]
            above = input[i - 1, j]

            try:
                next = input[i, j + 1]
                diag_forw = input[i - 1, j + 1]
            except IndexError:
                next = 0 
                diag_forw = 0
            try:
                prev = input[i, j - 1]
                diag_back = input[i - 1, j - 1]
            except IndexError:
                prev = 0 
                diag_back = 0

            if pos == 0:
                if (above == -2):
                    input[i, j] += 1 
                if above > 0:
                    input[i, j] = above
                if (next == -1 and diag_forw > 0):
                    input[i, j] += diag_forw 
                if (prev == -1 and diag_back > 0):
                    input[i, j] += diag_back 
    return input

def count_and_remove_splits(input):
    score = 0
    for i in range(1, len(input)):
        for j in range(len(input[0])):
            pos = input[i, j]
            above = input[i - 1, j]
            if pos == "^":
                if above == "|":
                    score += 1
                else:
                    input[i, j] = '.'
            
    return score, input

def to_ints(input):
    mapje = {".": 0, "|": 1, "^": -1, "S": -2}
    new_tree = np.zeros((len(input), len(input[0])))
    for i in range(0, len(input)):
        for j in range(len(input[0])):
            new_tree[i,j] = mapje[input[i,j]]

    return new_tree

def main_1(file):
    input = np.array([list(x) for x in np.loadtxt(file, dtype=str)])
    input = run_tachyon(input)
    count, input = count_and_remove_splits(input)
    return count

def main_2(file):
    input = np.array([list(x) for x in np.loadtxt(file, dtype=str)])
    input = to_ints(input)
    input = run_int_tachyon(input)
    return sum(input[-1])


if __name__ == "__main__":
    TEST_1_ANS = 21
    TEST_2_ANS = 40
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

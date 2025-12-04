import numpy as np
import os
import re
import math
from pathlib import Path
import itertools

opperations = {"R": lambda x,y: x+y, "L": lambda x,y: x-y}


def main_1(file):
    score = 0
    dial = 50
    input = np.loadtxt(file, dtype=str)
    input = map(lambda x: (x[0], int(x[1:])), input)
    for dir, num in input:
        dial = opperations[dir](dial, num) % 100
        if dial == 0:
            score +=1 
    return score

def main_2(file):
    print()
    score = 0
    dial = 50
    input = np.loadtxt(file, dtype=str)
    input = map(lambda x: (x[0], int(x[1:])), input)
    for dir, num in input:

        new_dial = opperations[dir](dial, num)
        print(f"{dial} {dir}{num} {new_dial}")

        if num == 0:
            continue

        if dial == 0 and dir == "L":
            score -= 1

        dial = new_dial % 100

        if dial == 0 and dir == "L":
            score +=1

        score += abs(new_dial  // 100)

        print(f"{new_dial = } {dial = } {score = } \n")
    return score


if __name__ == "__main__":
    TEST_1_ANS = 3 
    TEST_2_ANS = 6
    advent_day = Path(os.path.basename(__file__)).stem
    file = f"input_{advent_day}.txt"
    test_file = f"test_input_{advent_day}.txt"

    test_1 = main_1(test_file)
    print(f"{test_1 = }")
    if test_1 == TEST_1_ANS: 
        result_1 =  main_1(file)
        print(f"{result_1 = }")

    test_2 = main_2(test_file)
    print(f"{test_2 = }")
    if test_2 == TEST_2_ANS:
        result_2 =  main_2(file)
        print(f"{result_2 = }")

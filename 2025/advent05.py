import numpy as np
import os
import re
import math
from pathlib import Path
import itertools


def update(reaches, a, b):
    for i, reach in enumerate(reaches):
        low, high = reach
        if low <= a <= high and low <= b <= high: 
            break
        if low <= b <= high: 
            #lower 
            reaches[i] = (a, high)
            continue
        if low <= a <= high: 
            # higher
            reaches[i] = (low, b) 
            continue

    reaches.append((a,b))
    reaches.sort()
    return reaches

def self_update(reaches):
    i = 0
    while i < len(reaches)-1:

        low, high = reaches[i]
        a, b = reaches[i+1]

        if high < a:
            i += 1
            continue

        if a <= high:
            if b <= high:
                reaches.pop(i+1)
            if b > high:
                reaches[i] = (low, b)
                reaches.pop(i+1)
    return reaches

def main_1(file):
    score = 0

    file = open(file, 'r')
    line = file.readline()
    a, b = map(int, line.strip().split("-"))
    reaches = [(a,b)]

    while line != "\n":
        line = file.readline()
        try:
            a, b = map(int, line.strip().split("-"))
        except ValueError:
            break
        
        reaches = update(reaches, a, b)
        reaches = self_update(reaches)

    line = file.readline() 
    while line:
        number = int(line)
        for low, high in reaches:
            if low <= number <= high:
                score += 1
        line = file.readline() 

    return score 

def main_2(file):
    score = 0

    file = open(file, 'r')
    line = file.readline()
    a, b = map(int, line.strip().split("-"))
    reaches = [(a,b)]

    while line != "\n":
        line = file.readline()
        try:
            a, b = map(int, line.strip().split("-"))
        except ValueError:
            break
        
        reaches = update(reaches, a, b)
        reaches = self_update(reaches)

    for a, b in reaches:
        score += b - a + 1

    return score


if __name__ == "__main__":
    TEST_1_ANS = 3 
    TEST_2_ANS = 14 
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

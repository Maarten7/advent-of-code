import numpy as np
import os
import re
from pathlib import Path


def all_posible_answers_1(array):
    if len(array) == 2:
        a, b = array
        yield a + b
        yield a * b
        return

    last_element = array[-1]
    for answer in all_posible_answers_1(array[:-1]):
        yield last_element + answer
        yield last_element * answer


def all_posible_answers(array):
    if len(array) == 2:
        a, b = array
        yield a + b
        yield a * b
        yield int(str(a) + str(b))
        return

    last_element = array[-1]
    for answer in all_posible_answers(array[:-1]):
        yield last_element + answer
        yield last_element * answer
        yield int(str(answer) + str(last_element))


def main_1(file):
    input = open(file, "r").readlines()
    input = [line.split() for line in input]
    input = [(int(line[0][:-1]), [int(arg) for arg in line[1:]]) for line in input]
    result = [ans for ans, array in input if ans in list(all_posible_answers_1(array))]
    return sum(result)


def main_2(file):
    input = open(file, "r").readlines()
    input = [line.split() for line in input]
    input = [(int(line[0][:-1]), [int(arg) for arg in line[1:]]) for line in input]
    result = [ans for ans, array in input if ans in list(all_posible_answers(array))]
    return sum(result)


if __name__ == "__main__":
    advent_day = Path(os.path.basename(__file__)).stem

    file = f"test_input_{advent_day}.txt"
    test_1 = main_1(file)
    print(test_1)
    if test_1 == 3749:
        file = f"input_{advent_day}.txt"
        print(main_1(file))

    file = f"test_input_{advent_day}.txt"
    test_2 = main_2(file)
    print(test_2)
    if test_2 == 11387:
        file = f"input_{advent_day}.txt"
        print(main_2(file))

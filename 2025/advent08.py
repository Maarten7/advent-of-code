import numpy as np
import os
import re
import math
from pathlib import Path
import itertools


def distance_matrix(input):
    distances = np.zeros((len(input), len(input)))
    for i, ci in enumerate(input):
        for j, cj in enumerate(input):
            if i >= j:
                distances[i, j] = np.inf
                continue
            xi, yi, zi = ci
            xj, yj, zj = cj
            distance = math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2 + (zi - zj) ** 2)
            distances[i, j] = distance
    return distances


def main_1(file, n=1000):
    input = [x.split(",") for x in np.loadtxt(file, dtype=str)]
    input = [(int(a), int(b), int(c)) for a, b, c in input]
    distances = distance_matrix(input)

    connections = set()
    connect_numbers = np.zeros((len(input)))
    for z in range(n):
        i, j = np.unravel_index(np.argmin(distances, axis=None), distances.shape)

        if i in connections and j in connections:
            # connect connections highest to lowest and friends
            con_num = min(connect_numbers[i], connect_numbers[j])
            connect_numbers[(np.where(connect_numbers == connect_numbers[i]))] = con_num
            connect_numbers[(np.where(connect_numbers == connect_numbers[j]))] = con_num
        elif i in connections and j not in connections:
            # connect b to a and friends
            con_num = connect_numbers[i]
            connect_numbers[j] = con_num
            connections.add(j)
        elif i not in connections and j in connections:
            # connect a to b and friends
            con_num = connect_numbers[j]
            connect_numbers[i] = con_num
            connections.add(i)
        else:
            connections.add(i)
            connections.add(j)
            con_num = connect_numbers.max() + 1
            connect_numbers[i] = con_num
            connect_numbers[j] = con_num

        distances[i, j] = np.inf

    connect_numbers = connect_numbers[np.where(connect_numbers != 0)]
    numbers, count = np.unique(connect_numbers, return_counts=True)
    return np.prod(sorted(count)[-3:])


def main_2(file, n=1000):
    input = [x.split(",") for x in np.loadtxt(file, dtype=str)]
    input = [(int(a), int(b), int(c)) for a, b, c in input]
    distances = distance_matrix(input)

    connections = set()
    connect_numbers = np.zeros((len(input)))

    k = 0
    while k < n or len(np.unique(connect_numbers)) != 1:
        k += 1
        i, j = np.unravel_index(np.argmin(distances, axis=None), distances.shape)

        if i in connections and j in connections:
            # connect connections highest to lowest and friends
            con_num = min(connect_numbers[i], connect_numbers[j])
            connect_numbers[(np.where(connect_numbers == connect_numbers[i]))] = con_num
            connect_numbers[(np.where(connect_numbers == connect_numbers[j]))] = con_num
        elif i in connections and j not in connections:
            # connect b to a and friends
            con_num = connect_numbers[i]
            connect_numbers[j] = con_num
            connections.add(j)
        elif i not in connections and j in connections:
            # connect a to b and friends
            con_num = connect_numbers[j]
            connect_numbers[i] = con_num
            connections.add(i)
        else:
            connections.add(i)
            connections.add(j)
            con_num = connect_numbers.max() + 1
            connect_numbers[i] = con_num
            connect_numbers[j] = con_num

        distances[i, j] = np.inf

    return input[i][0] * input[j][0]


if __name__ == "__main__":
    TEST_1_ANS = 40
    TEST_2_ANS = 25272
    advent_day = Path(os.path.basename(__file__)).stem
    file = f"input_{advent_day}.txt"
    test_file = f"test_input_{advent_day}.txt"

    test_1 = main_1(test_file, n=10)
    print(f"{test_1 = }")
    if test_1 == TEST_1_ANS:
        result_1 = main_1(file)
        print(f"{result_1 = }")

    test_2 = main_2(test_file, n=10)
    print(f"{test_2 = }")
    if test_2 == TEST_2_ANS:
        result_2 = main_2(file)
        print(f"{result_2 = }")

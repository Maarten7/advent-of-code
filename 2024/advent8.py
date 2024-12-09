import numpy as np
import os
import re
from pathlib import Path

import itertools


def main_1(file):
    input = np.loadtxt(file, dtype=str)
    input = np.array([list(line) for line in input], dtype=str)
    nodes = np.zeros(input.shape)
    max_i, max_j = input.shape
    antennas = np.unique(input)
    antennas = np.delete(antennas, np.where(antennas == "."))

    node_set = set()
    for antenna in antennas:
        locations = np.where(input == antenna)
        locations = np.dstack(locations)[0]
        for duo in itertools.combinations(locations, 2):
            a, b = duo
            dist = b - a
            for node in [a - dist, b + dist]:
                node = tuple(node)
                i, j = node
                if 0 <= i < max_i and 0 <= j < max_j:
                    node_set.add(node)
                    if input[node] == ".":
                        input[node] = "#"

    return len(node_set)


def main_2(file):
    input = np.loadtxt(file, dtype=str)
    input = np.array([list(line) for line in input], dtype=str)
    nodes = np.zeros(input.shape)
    max_i, max_j = input.shape
    antennas = np.unique(input)
    antennas = np.delete(antennas, np.where(antennas == "."))

    node_set = set()
    for antenna in antennas:
        locations = np.where(input == antenna)
        locations = np.dstack(locations)[0]
        for duo in itertools.combinations(locations, 2):
            a, b = duo
            dist = b - a

            p = 0
            node = tuple(a - p * dist)
            while 0 <= node[0] < max_i and 0 <= node[1] < max_j:
                node_set.add(node)
                if input[node] == ".":
                    input[node] = "#"
                p += 1
                node = tuple(a - p * dist)

            p = 1
            node = tuple(a + p * dist)
            while 0 <= node[0] < max_i and 0 <= node[1] < max_j:
                node_set.add(node)
                if input[node] == ".":
                    input[node] = "#"
                p += 1
                node = tuple(a + p * dist)

    print("\n".join(["".join(line) for line in input]))
    return len(node_set)


if __name__ == "__main__":
    advent_day = Path(os.path.basename(__file__)).stem

    file = f"test_input_{advent_day}.txt"
    test_1 = main_1(file)
    print(test_1)
    if test_1 == 14:
        file = f"input_{advent_day}.txt"
        print(main_1(file))

    file = f"test_input_{advent_day}.txt"
    test_2 = main_2(file)
    print(test_2)
    if test_2 == 34:
        file = f"input_{advent_day}.txt"
        print(main_2(file))

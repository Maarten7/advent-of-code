import numpy as np
import os
import re
from pathlib import Path
import itertools


def get_neighbours(point, input):
    max_i, max_j = input.shape
    i, j = point
    neighbours = []
    if 0 < i:
        neighbours.append((i - 1, j))
    if i < max_i - 1:
        neighbours.append((i + 1, j))
    if 0 < j:
        neighbours.append((i, j - 1))
    if j < max_j - 1:
        neighbours.append((i, j + 1))
    return neighbours


def find_paths(path, input):
    last_location = path[-1]

    if input[last_location] == 9:
        yield path
        return

    neighbours = get_neighbours(last_location, input)
    for neighbour in neighbours:
        if input[neighbour] - input[last_location] == 1:
            for _path in find_paths(path + [neighbour], input):
                yield _path


def main_1(file):
    input = np.array(
        [[int(x) for x in list(line)] for line in np.loadtxt(file, dtype=str)]
    )
    iis, jjs = np.where(input == 0)
    trail_heads = list(zip(iis.tolist(), jjs.tolist()))
    summ = 0

    for trail_head in trail_heads:
        reached_peaks = set()
        for path in find_paths([trail_head], input):
            reached_peaks.add(path[-1])

        summ += len(reached_peaks)

    return summ


def main_2(file):
    input = np.array(
        [[int(x) for x in list(line)] for line in np.loadtxt(file, dtype=str)]
    )
    iis, jjs = np.where(input == 0)
    trail_heads = list(zip(iis.tolist(), jjs.tolist()))
    summ = 0

    for trail_head in trail_heads:
        summ += len(list(find_paths([trail_head], input)))

    return summ


if __name__ == "__main__":
    advent_day = Path(os.path.basename(__file__)).stem

    file = f"test_input_{advent_day}.txt"
    test_1 = main_1(file)
    print(test_1)
    if test_1 == 36:
        file = f"input_{advent_day}.txt"
        print(main_1(file))

    file = f"test_input_{advent_day}.txt"
    test_2 = main_2(file)
    print(test_2)
    if test_2 == 81:
        file = f"input_{advent_day}.txt"
        print(main_2(file))

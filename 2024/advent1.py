import numpy as np
import os
from pathlib import Path


def main_1(file):
    input = np.loadtxt(file, dtype=int)
    sorted_input = np.sort(input, axis=0)
    distances = np.diff(sorted_input)
    return np.sum(np.abs(distances))


def main_2(file):
    input = np.loadtxt(file, dtype=int)
    left = input[:, 0]
    right = input[:, 1]
    unique, counts = np.unique(right, return_counts=True)
    counts = dict(zip(unique, counts))

    return sum(map(lambda el: el * counts.get(el, 0), left))


if __name__ == "__main__":
    advent_day = Path(os.path.basename(__file__)).stem

    part_1 = main_1(f"test_input_{advent_day}.txt")
    print(part_1)
    assert part_1 == 11
    print(main_1(f"input_{advent_day}.txt"))

    part_2 = main_2(f"test_input_{advent_day}.txt")
    print(part_2)
    assert part_2 == 31
    print(main_2(f"input_{advent_day}.txt"))

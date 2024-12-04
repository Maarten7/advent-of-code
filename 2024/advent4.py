import numpy as np
import os
import re
from pathlib import Path

def count_xmas(letters: str):
    counts = re.findall("XMAS", letters)
    return len(counts)

def main_1(file):
    total = 0
    input = np.loadtxt(file, dtype=str)
    input = np.array([list(string) for string in input])

    total += sum([count_xmas("".join(inpu)) for inpu in input])
    total += sum([count_xmas("".join(inpu)) for inpu in input[:, ::-1]])
    total += sum([count_xmas("".join(inpu)) for inpu in input.T])
    total += sum([count_xmas("".join(inpu)) for inpu in input.T[:, ::-1]])

    for offset in range(-input.shape[0], input.shape[0] ):
        total += count_xmas("".join(np.diagonal(input, offset=offset)))
        total += count_xmas("".join(np.diagonal(input, offset=offset))[::-1])
        total += count_xmas("".join(np.diagonal(input[:, ::-1], offset=offset)))
        total += count_xmas("".join(np.diagonal(input[:, ::-1], offset=offset))[::-1])

    return total


def main_2(file):
    total = 0
    input = np.loadtxt(file, dtype=str)
    input = np.array([list(string) for string in input])

    letters = set(["M", "S"])

    for i, j in np.dstack(np.where(input == 'A')).reshape(-1, 2):

        if i in [0, input.shape[0] - 1] or j in [0, input.shape[1] - 1]:
            continue

        lu = input[i-1, j-1]
        ld = input[i-1, j+1]
        ru = input[i+1, j-1]
        rd = input[i+1, j+1]


        if set([lu, rd]) == letters and set([ld, ru]) == letters:
            total += 1

    return total

if __name__ == "__main__":
    advent_day = Path(os.path.basename(__file__)).stem

    file = f"test_input_{advent_day}.txt"

    test_1 = main_1(file)
    print(test_1)
    if test_1 == 18:
        file = f"input_{advent_day}.txt"
        print(main_1(file))

    test_2 = main_2(file)
    print(test_2)
    if test_2 == 9:
        file = f"input_{advent_day}.txt"
        print(main_2(file))
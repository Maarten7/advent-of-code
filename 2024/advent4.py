import numpy as np
import os
from pathlib import Path


def main_1(array):
    pass

def main_2(array):
    pass


if __name__ == "__main__":
    advent_day = Path(os.path.basename(__file__)).stem

    file = f"test_input_{advent_day}.txt"
    input = np.loadtxt(file, dtype=int)

    test_1 = main_1(input); print(test_1)
    if test_1 == 0:
        input = np.loadtxt(f"input_{advent_day}.txt", dtype=int)
        print(main_1(input))

    test_2 = main_2(input)
    if test_2 == 0:
        input = np.loadtxt(f"input_{advent_day}.txt", dtype=int)
        print(main_2(input))
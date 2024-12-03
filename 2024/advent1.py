import numpy as np
import os
from pathlib import Path


def main(file):
    with open(file, 'r') as lines:
        for line in lines:

    return

if __name__ == "__main__":
    advent_day = Path(os.path.basename(__file__)).stem
    test = main(f"test_input_{advent_day}.txt")
    print(test)
    assert test == 0
    print(main(f"input_{advent_day}.txt"))
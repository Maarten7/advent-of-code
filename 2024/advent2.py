import numpy as np
import os
from pathlib import Path


def is_safe(regel):
    safe = True
    allowed_diffs = np.array([1, 2, 3])
    diffs = np.unique(np.diff(regel))

    abs_diffs = np.abs(diffs)
    are_allowed = np.isin(abs_diffs, allowed_diffs)
    if not np.all(are_allowed):
        safe = False

    all_positive = np.all(diffs > 0)
    all_negative = np.all(diffs < 0)
    if not (all_positive or all_negative):
        safe = False

    return safe


def is_safer(regel):
    for i in range(len(regel)):
        new_regel = regel[0:i] + regel[i + 1 :]
        safe = is_safe(new_regel)

        if safe:
            return safe


def main(file):
    with open(file, "r") as lines:

        safe_count = 0
        for line in lines.readlines():

            regel = [int(num) for num in line.split()]

            if is_safer(regel):
                safe_count += 1

    return safe_count


if __name__ == "__main__":
    advent_day = Path(os.path.basename(__file__)).stem
    test = main(f"test_input_{advent_day}.txt")
    print(test)
    assert test == 4
    print(main(f"input_{advent_day}.txt"))

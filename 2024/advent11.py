import numpy as np
import os
import re
from pathlib import Path
import itertools
from functools import lru_cache

# {(stone, depth): total_resulting_stones}
# {(0, 3), 4}
LOOKUP = {}


@lru_cache(maxsize=100000)
def total_stones(stone, n=25):
    stones = [stone]
    for _ in range(n):

        update = []
        for stone in stones:
            num_digits = len(str(stone))

            if stone == 0:
                update.append(1)

            elif num_digits % 2 == 0:

                half = num_digits // 2
                a = str(stone)[:half]
                b = str(stone)[half:]

                update.extend([int(a), int(b)])

            else:
                update.append(stone * 2024)

        stones = update

    return len(stones), stones


def go_deep(stones, depth):

    step_size = 5
    total = 0

    if depth == step_size:
        for stone in stones:

            sub_total = LOOKUP.setdefault(
                (stone, depth), total_stones(stone, step_size)[0]
            )
            total += sub_total

        return total

    else:
        for stone in stones:

            result = LOOKUP.get((stone, depth))

            if result == None:
                _, new_stones = total_stones(stone, step_size)
                result = go_deep(new_stones, depth - step_size)
                LOOKUP[(stone, depth)] = result

            total += result

        return total


def main_1(file):
    input = [int(i) for i in open(file).readline().split()]
    total = sum([total_stones(stone)[0] for stone in input])
    return total


def main_2(file):
    input = [int(i) for i in open(file).readline().split()]
    stones = input
    return go_deep(stones, 75)


if __name__ == "__main__":
    advent_day = Path(os.path.basename(__file__)).stem

    file = f"test_input_{advent_day}.txt"
    test_1 = main_1(file)
    print(f"{test_1 = }")
    if test_1 == 55312:
        file = f"input_{advent_day}.txt"
        print(f"{main_1(file) = }")

    file = f"test_input_{advent_day}.txt"
    test_2 = main_2(file)
    print(f"{test_2 = }")
    if test_2:
        file = f"input_{advent_day}.txt"
        print(f"{main_2(file) = }")

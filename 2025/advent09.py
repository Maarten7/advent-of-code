import numpy as np
import os
import re
import math
from pathlib import Path
import itertools


def get_outside(tiles):
    rx, ry = tiles.shape

    print(tiles)
    for i in range(rx):
        if i % 1000 == 0:
            print(i, rx)
        xs, = np.where(tiles[i] == 2)
        if xs.size:
            print(xs)
    
    return np.where(tiles == 1)


def connect_dots(input):
    xs, ys = list(zip(*input))
    tiles = np.zeros((max(xs) + 1, max(ys) + 1))

    for i in range(-1, len(input) - 1):
        x, y = input[i]
        a, b = input[i + 1]

        tiles[x, y] = 2 
        if a == x:
            tiles[a, min(y, b): max(y, b)] = 2 
        if b == y:
            tiles[min(x, a): max(x, a), b] = 2 

    return tiles


def get_areas(input):
    areas = np.zeros((len(input), len(input)))
    for i, ci in enumerate(input):
        for j, cj in enumerate(input):
            if i > j:
                continue
            areas[i, j] = (abs(ci[0] - cj[0]) + 1) * (abs(ci[1] - cj[1]) + 1)
    return areas


def main_1(file):
    input = [x.split(",") for x in np.loadtxt(file, dtype=str)]
    input = [(int(a), int(b)) for a, b in input]
    areas = get_areas(input)
    return areas.max()


def main_2(file):
    input = np.loadtxt(file, dtype=str)
    input = [x.split(",") for x in np.loadtxt(file, dtype=str)]
    input = [(int(a), int(b)) for a, b in input]
    areas = get_areas(input)
    tiles = connect_dots(input)
    outside = get_outside(tiles)
    outy, outx = outside

    while True:
        a, b = np.unravel_index(np.argmax(areas, axis=None), areas.shape)

        ai, aj = input[a]
        bi, bj = input[b]

        has_outsider_on_border = False
        for y in outy[np.where(outx == bj)]:
            if min(ai, bi) < y < max(ai, bi):
                has_outsider_on_border = True
                break
        for y in outy[np.where(outx == aj)]:
            if has_outsider_on_border:
                break
            if min(ai, bi) < y < max(ai, bi):
                has_outsider_on_border = True
                break
        for x in outx[np.where(outy == bi)]:
            if has_outsider_on_border:
                break
            if min(aj, bj) < x < max(aj, bj):
                has_outsider_on_border = True
                break
        for x in outx[np.where(outy == ai)]:
            if has_outsider_on_border:
                break
            if min(aj, bj) < x < max(aj, bj):
                has_outsider_on_border = True
                break

        if has_outsider_on_border:
            areas[a, b] = 0
            continue

        if not has_outsider_on_border:
            return areas[a, b]


if __name__ == "__main__":
    TEST_1_ANS = 50
    TEST_2_ANS = 24
    advent_day = Path(os.path.basename(__file__)).stem
    file = f"input_{advent_day}.txt"
    test_file = f"test_input_{advent_day}.txt"

    test_1 = main_1(test_file)
    print(f"{test_1 = }")
    if test_1 == TEST_1_ANS:
        result_1 = main_1(file)
        print(f"{result_1 = }")

    test_2 = main_2(test_file)
    print(f"{test_2 = }")
    if test_2 == TEST_2_ANS:
        result_2 = main_2(file)
        print(f"{result_2 = }")

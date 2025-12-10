import numpy as np
import os
from pathlib import Path


def get_rectangle_lines(input, a, b):
    ax, ay = input[a]
    bx, by = input[b]
    return (
        (ax, (min(ay, by), max(ay, by))),
        (bx, (min(ay, by), max(ay, by))),
        ((min(ax, bx), max(ax, bx)), ay),
        ((min(ax, bx), max(a, ax)), by),
    )


def lines_clean(lines, tiles):

    x_line_1, x_line_2, y_line_1, y_line_2 = lines

    for x_line in [x_line_1, x_line_2]:
        x_value, (y_low, y_high) = x_line
        (ys,) = np.where(tiles[x_value] != 2)
        if ys.size:
            if set(ys) & set(range(y_low, y_high + 1)):
                return False

    for y_line in [y_line_1, y_line_2]:
        (x_low, x_high), y_value = y_line
        (xs,) = np.where(tiles[:, y_value] != 2)
        if xs.size:
            if set(xs) & set(range(x_low, x_high + 1)):
                return False
    return True


def connect_dots(input):
    xs, ys = list(zip(*input))
    tiles = np.zeros((max(xs) + 1, max(ys) + 1))

    for i in range(-1, len(input) - 1):
        x, y = input[i]
        a, b = input[i + 1]

        tiles[x, y] = 2
        if a == x:
            tiles[a, min(y, b) : max(y, b)] = 2
        if b == y:
            tiles[min(x, a) : max(x, a), b] = 2

    return tiles


def fill_shape(tiles):
    ri, rj = tiles.shape
    for i in range(ri):
        if i % 1000 == 0:
            print(i, ri)
        inside = False
        for j in range(rj):
            if tiles[i, j] == 2:
                inside = not inside
            if tiles[i, j] == 0:
                if inside:
                    tiles[i, j] = 2

    return tiles


def get_areas(input):
    areas = np.empty((len(input), len(input)), dtype=int)
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
    tiles = fill_shape(tiles)
    print("shaped filled")

    a, b = np.unravel_index(np.argmax(areas, axis=None), areas.shape)
    four_lines = get_rectangle_lines(input, a, b)

    k = 0
    while not lines_clean(four_lines, tiles):
        areas[a, b] = 0
        a, b = np.unravel_index(np.argmax(areas, axis=None), areas.shape)
        four_lines = get_rectangle_lines(input, a, b)

        if k % 100 == 0:
            print(k, int(0.5 * len(input) ** 2))
        k += 1

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

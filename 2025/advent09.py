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
        ys, = np.where(tiles[x_value] == 2)
        if ys.size:
            first_2 = ys[0]
            last_2 = ys[-1]
            if y_low < first_2:
                return False
            if last_2 < y_high: 
                return False
        else:
            return False
        for y_value in range(y_low, y_high + 1):
            xs, = np.where(tiles[:, y_value] == 2)
            if xs.size:
                first_2 = xs[0]
                last_2 = xs[-1]
                if x_value < first_2 or last_2 < x_value:
                    return False
            else:
                return False
    
    for y_line in [y_line_1, y_line_2]:
        (x_low, x_high), y_value = y_line
        xs, = np.where(tiles[:, y_value] == 2)
        if xs.size:
            first_2 = xs[0]
            last_2 = xs[-1]
            if x_low < first_2:
                return False
            if last_2 < x_high: 
                return False
        else:
            return False
        for x_value in range(x_low, x_high+1):
            ys, = np.where(tiles[x_value] == 2)
            if ys.size:
                first_2 = ys[0]
                last_2 = ys[-1]
                if y_value < first_2 or last_2 < y_value:
                    return False
            else:
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


def get_areas(input):
    areas = np.empty((len(input), len(input)), dtype=int)
    for i, ci in enumerate(input):
        for j, cj in enumerate(input):
            if i > j:
                continue
            areas[i, j] = (abs(ci[0] - cj[0]) + 1) * (abs(ci[1] - cj[1]) + 1)
    return areas


def get_rectangle_perimeter(input, a, b):
    ax, ay = input[a]
    bx, by = input[b]

    square = set()
    square.update({(ax, j) for j in range(min(ay, by), max(ay, by))})
    square.update({(i, ay) for i in range(min(ax, bx), max(ax, bx))})
    square.update({(bx, j) for j in range(min(ay, by), max(ay, by))})
    square.update({(i, by) for i in range(min(ax, bx), max(ax, bx))})

    return square



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

    a, b = np.unravel_index(np.argmax(areas, axis=None), areas.shape)
    four_lines = get_rectangle_lines(input, a, b)

    while not lines_clean(four_lines, tiles):
        areas[a, b] = 0
        a, b = np.unravel_index(np.argmax(areas, axis=None), areas.shape)
        four_lines = get_rectangle_lines(input, a, b)

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

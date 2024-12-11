import numpy as np

directions = [UP, DOWN, RIGHT, LEFT] = [(-1, 0), (1, 0), (0, 1), (0, -1)]
direction_str = {UP: "^", DOWN: "v", RIGHT: ">", LEFT: "<"}
forward_mirror = {UP: RIGHT, DOWN: LEFT, RIGHT: UP, LEFT: DOWN}
backward_mirror = {UP: LEFT, DOWN: RIGHT, RIGHT: DOWN, LEFT: UP}

grid = np.array([list(line.strip()) for line in open("advent16.txt")])
max_i, max_j = grid.shape


def in_bound(position):
    i, j = position
    return 0 <= i < max_i and 0 <= j < max_j

def calculate_energy(pos, dir):

    history = set()
    energy = np.zeros(shape=grid.shape)

    def run_light(position, direction):

        while True:
            if (position, direction) in history:
                return

            history.add((position, direction))
            energy[position] = 1

            tile = grid[position]

            if tile == "\\":
                direction = backward_mirror[direction]
            if tile == "/":
                direction = forward_mirror[direction]

            if (direction, tile) in [
                (UP, "-"),
                (DOWN, "-"),
            ]:
                run_light(position, LEFT)
                run_light(position, RIGHT)
                return

            if (direction, tile) in [
                (RIGHT, "|"),
                (LEFT, "|"),
            ]:
                run_light(position, UP)
                run_light(position, DOWN)
                return

            i, j = position
            di, dj = direction
            position = i + di, j + dj
            if not in_bound(position):
                return

    run_light(pos, dir)
    return int(energy.sum())


print(calculate_energy((0, 0), RIGHT))

def part_2():
    most_energy = 0
    most_energy = max(
        most_energy, max([calculate_energy((i, 0), RIGHT) for i in range(max_i)])
    )
    most_energy = max(
        most_energy, max([calculate_energy((max_i - 1, 0), LEFT) for i in range(max_i)])
    )
    most_energy = max(
        most_energy, max([calculate_energy((0, j), DOWN) for j in range(max_j)])
    )
    most_energy = max(
        most_energy, max([calculate_energy((0, max_j - 1), UP) for i in range(max_i)])
    )
    return most_energy


print(part_2())
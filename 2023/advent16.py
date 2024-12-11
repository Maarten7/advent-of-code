import numpy as np

DOWN = (1, 0)
UP = (-1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)
directions = [UP, DOWN, RIGHT, LEFT]
direction_str = {UP: "^", DOWN: "v", RIGHT: ">", LEFT: "<"}
forward_mirror = {UP: RIGHT, DOWN: LEFT, RIGHT: UP, LEFT: DOWN}
backward_mirror = {UP: LEFT, DOWN: RIGHT, RIGHT: DOWN, LEFT: UP}

grid = np.array([list(line.strip()) for line in open("advent16.txt")])
max_i, max_j = grid.shape


def re_run_light(pos, dir):
    history = set()
    energy = np.zeros(shape=grid.shape)


    def update_position(position, direction):
        i, j = position
        di, dj = direction
        new_position = i + di, j + dj
        return new_position


    def update_direction(position, direction):
        item = grid[position]

        if item == "\\":
            return backward_mirror[direction]
        if item == "/":
            return forward_mirror[direction]

        if (direction, item) in [
            (UP, "-"),
            (DOWN, "-"),
        ]:
            run_light(position, LEFT)
            run_light(position, RIGHT)
            return

        if (direction, item) in [
            (RIGHT, "|"),
            (LEFT, "|"),
        ]:
            run_light(position, UP)
            run_light(position, DOWN)
            return

        return direction


    def in_bound(position):
        i, j = position
        return 0 <= i < max_i and 0 <= j < max_j


    def run_light(position, direction):

        while True:
            if (position, direction) in history:
                return

            history.add((position, direction))
            energy[position] = 1

            direction = update_direction(position, direction)
            if not direction:
                return

            position = update_position(position, direction)
            if not in_bound(position):
                return

    run_light(pos, dir)
    return int(energy.sum())

print(re_run_light((0, 0), RIGHT))

most_energy = 0
most_energy = max(most_energy, max([re_run_light((i, 0), RIGHT) for i in range(max_i)]))
most_energy = max(most_energy, max([re_run_light((max_i - 1, 0), LEFT) for i in range(max_i)]))
most_energy = max(most_energy, max([re_run_light((0, j), DOWN) for j in range(max_j)]))
most_energy = max(most_energy, max([re_run_light((0, max_j - 1), UP) for i in range(max_i)]))
print(most_energy)
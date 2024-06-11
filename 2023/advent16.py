import numpy as np

grid = []
history = []
for line in open("advent161.txt"):
    grid.append(list(line.strip()))

grid = np.array(grid)
history = [[set() for j in range(len(grid[0]))] for i in range(len(grid))]
history = np.array(history)
draw = np.full(shape=grid.shape, fill_value=".")
energy = np.zeros(shape=grid.shape)
energy_draw = np.full(shape=grid.shape, fill_value='.')


def update_position(i, j, direction):
    if direction == ">":
        if j + 1 >= len(grid[0]):
            return
        return i, j + 1
    if direction == "<":
        if j -1 < 0:
            return
        return i, j - 1
    if direction == "^":
        if i - 1 < 0:
            return
        return i - 1, j
    if direction == "v":
        if i + 1 >= len(grid):
            return
        return i + 1, j


def update_direction(position, direction):
    item = grid[position]

    energy[position] = 1
    if item == ".":
        draw[position] = direction
        return direction
    if item == "\\":
        mirror = {">": "v", "<": "^", "^": "<", "v": ">"}
        return mirror[direction]
    if item == "/":
        mirror = {">": "^", "<": "v", "^": ">", "v": "<"}
        return mirror[direction]

    if (direction, item) in [
        (">", "-"),
        ("<", "-"),
        ("^", "|"),
        ("v", "|"),
    ]:
        return direction

    if (direction, item) in [
        ("^", "-"),
        ("v", "-"),
    ]:
        run_light(position, "<")
        run_light(position, ">")
        return
    if (direction, item) in [
        (">", "|"),
        ("<", "|"),
    ]:
        run_light(position, "^")
        run_light(position, "v")
        return

def run_light(position, direction):
    i, j = position
    energy[position] = 1
    energy_draw[position] = '#'
    if i < 0 or j < 0:
        return
    if i >= len(grid) or j >= len(grid[0]):
        return

    while 1:
        draw[position] = direction 
        print(draw)
        if direction in history[position]:
            return
        history[position].add(direction)

        position = update_position(*position, direction=direction)
        if not position:
            break

        direction = update_direction(position, direction)
        if not direction:
            return

        energy[position] = 1
        energy_draw[position] = '#'


print(grid)
print()

run_light((0, 0), ">")
print(draw)
print()
print(energy_draw)
print(int(energy.sum()))

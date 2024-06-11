import numpy as np


def is_symmetrical(grid, orientation):
    if orientation == "horizontal":
        for axis in range(1, len(grid)):
            smudges = 0
            for i in range((min(axis, len(grid) - axis))):
                for j in range(len(grid[0])):
                    if grid[axis - i - 1, j] != grid[axis + i, j]:
                        smudges += 1
            if smudges == 1:
                return axis

    if orientation == "vertical":
        for axis in range(1, len(grid[0])):
            smudges = 0
            for j in range((min(axis, len(grid[0]) - axis))):
                for i in range(len(grid)):
                    if grid[i, axis - j - 1] != grid[i, axis + j]:
                        smudges += 1
            if smudges == 1:
                return axis
    return 0


grid = []
som = 0
for line in open("advent13.txt"):
    line = line.strip()
    print(line)
    if not line:
        grid = np.array(grid)
        axis_num = is_symmetrical(grid, orientation="horizontal")
        som += 100 * axis_num
        print("horizontal", axis_num)
        axis_num = is_symmetrical(grid, orientation="vertical")
        som += axis_num
        print("vertical", axis_num)
        grid = []
    else:
        grid.append(list(line))

print(som)

import numpy as np


def cycle(beams):
    beams = north(beams)
    beams = west(beams)
    beams = south(beams)
    beams = east(beams)
    return beams


def north(beams):
    z = np.array(beams.copy())
    for j in range(len(beams[0])):
        z[:, j] = tilt(beams[:, j])
    return z.copy()


def east(beams):
    z = np.array(beams.copy())
    for i in range(len(beams)):
        z[i, ::-1] = tilt(beams[i, ::-1])
    return z.copy()


def south(beams):
    # south
    z = np.array(beams.copy())
    for j in range(len(beams[0])):
        z[::-1, j] = tilt(beams[::-1, j])
    return z.copy()


def west(beams):
    z = np.array(beams.copy())
    for i in range(len(beams)):
        z[i, :] = tilt(beams[i, :])
    return z.copy()


def calculate_support(beams):
    som = 0
    for i, row in enumerate(beams):
        for char in row:
            if char == "O":
                som += len(beams) - i
    return som


def tilt(column):
    for i in range(len(column)):
        if column[i] == "O":
            z = i
            while z > 0:
                z = z - 1
                if column[z] == "#" or column[z] == "O":
                    column[i] = "."
                    column[z + 1] = "O"
                    break
                if z == 0 and i != 0:
                    column[i] = "."
                    column[z] = "O"
                    break
    return column


grid = []
for line in open("advent14.txt"):
    line = line.strip()
    grid.append(list(line))
print("-----------------------")
beams = np.array(grid)

support_cycle = [
    84206,
    84202,
    84191,
    84210,
    84220,
    84237,
    84244,
    84276,
    84294,
    84328,
    84341,
    84341,
    84332,
    84332,
    84314,
    84299,
    84268,
    84239,
]

m = 1000000000
print(support_cycle[(m - 162) % len(support_cycle) - 1])
# start cyclus = 162
for i in range(1, m + 1):
    beams = cycle(beams)
    support = calculate_support(beams)

    if i == m:
        print(support)

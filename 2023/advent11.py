import math

grid = []
for line in open("advent11.txt"):
    grid.append(line.strip())

extra_rows = []
for i in range(len(grid)):
    if "#" not in grid[i]:
        extra_rows.append(i)
        continue

extra_columns = []
for j in range(len(grid[0])):
    empty = True
    for i in range(len(grid)):
        if grid[i][j] == "#":
            empty = False
    if empty:
        extra_columns.append(j)


def add_empty():
    for k, i in enumerate(extra_rows):
        grid.insert(i + k, grid[i + k])

    for k, j in enumerate(extra_columns):
        for i in range(len(grid)):
            row = list(grid[i])
            row.insert(j + k, ".")
            grid[i] = row


print("\n".join(["".join(k) for k in grid]))


def get_symbol(i, j):
    return grid[i][j]


def get_positions():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            yield i, j


galaxies = []
for pos in get_positions():
    if get_symbol(*pos) == "#":
        galaxies.append(pos)


factor = 1_000_000
som = 0
for i, galaxy1 in enumerate(galaxies):
    for j, galaxy2 in enumerate(galaxies):
        if j <= i:
            continue
        else:
            distance = 0
            y1, x1 = galaxy1
            y2, x2 = galaxy2
            distance = abs(y2 - y1)

            for row in extra_rows:
                if row in range(min(y2, y1) + 1, max(y2, y1)):
                    distance += factor - 1

            distance += abs(x2 - x1)

            for column in extra_columns:
                if column in range(min(x2, x1) + 1, max(x2, x1)):
                    distance += factor - 1
            som += distance
print(som)

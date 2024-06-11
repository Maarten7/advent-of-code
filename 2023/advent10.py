grid = []
for i, line in enumerate(open("advent10.txt")):
    grid.append(line.strip())

    if "S" in line:
        start = i, line.index("S")


def goes_on(a, b, pos):
    possible_combination = [
        ("F", "-", (0, 1)),
        ("F", "|", (1, 0)),
        ("F", "7", (0, 1)),
        ("F", "J", (0, 1)),
        ("F", "J", (1, 0)),
        ("F", "L", (1, 0)),
        ("7", "-", (0, -1)),
        ("7", "|", (1, 0)),
        ("7", "J", (1, 0)),
        ("7", "L", (1, 0)),
        ("7", "L", (0, -1)),
        ("J", "-", (0, -1)),
        ("J", "|", (-1, 0)),
        ("J", "L", (0, -1)),
        ("L", "-", (0, 1)),
        ("L", "|", (-1, 0)),
        ("|", "|", (1, 0)),
        ("-", "-", (0, 1)),
    ]

    if (a, b, pos) in possible_combination or (
        b,
        a,
        (pos[0] * -1, pos[1] * -1),
    ) in possible_combination:
        return True
    return False


def get_surround(i, j):
    yield i + 1, j, (1, 0)
    yield i, j - 1, (0, -1)
    yield i - 1, j, (-1, 0)
    yield i, j + 1, (0, 1)


def get_neighbours(i, j):
    for i, j, _ in get_surround(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            yield i, j


def get_positions():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            yield i, j


def get_symbol(i, j):
    try:
        return grid[i][j]
    except IndexError:
        return


def get_next_position(position, last_position):
    for i, j, pos in get_surround(*position):
        posible_next = i, j
        posible_next_sym = get_symbol(*posible_next)
        current_symbol = get_symbol(*position)
        if (
            goes_on(current_symbol, posible_next_sym, pos)
            and posible_next != last_position
        ):
            next = posible_next
            return next


first = (start[0] - 1, start[1])
end = (start[0], start[1] + 1)


path = [start, first]
position = path[-1]
while position != end:
    position = get_next_position(position=position, last_position=path[-2])
    path.append(position)
print(len(path) / 2)

path = set(path)
outsiders = set()
insiders = set()

for i in range(len(grid)):
    inside = False
    open_symbol = ""
    close_symbol = ""
    for j in range(len(grid[0])):
        curr = (i, j)
        potential = curr not in path

        if curr in path:
            curr_sym = get_symbol(*curr)
            if curr_sym == "|":
                inside = not inside
                continue
            if curr_sym == "-":
                continue
            if curr_sym in ["F", "L"]:
                open_symbol = curr_sym
                continue
            if curr_sym in ["J", "7"]:
                close_symbol = curr_sym
                match (open_symbol, close_symbol):
                    case ("F", "J"):
                        inside = not inside
                    case ("L", "7"):
                        inside = not inside
        else:
            if inside:
                insiders.add(curr)

dgrid = []
for i in range(len(grid)):
    dgrid.append(" " * len(grid[0]))

for pos in path:
    i, j = pos
    k = list(dgrid[i])
    k[j] = "X"
    # k[j] = get_symbol(i,j)
    dgrid[i] = "".join(k)

for pos in insiders:
    i, j = pos
    k = list(dgrid[i])
    k[j] = "I"
    dgrid[i] = "".join(k)

for pos in outsiders:
    i, j = pos
    k = list(dgrid[i])
    k[j] = "O"
    dgrid[i] = "".join(k)

print("\n".join(dgrid))
print(len(insiders))

inputt = [[char for char in line] for line in open("advent3.txt")]
symbols = ["/", "&", "@", "-", "#", "=", "*", "+", "%", "$"]


def has_symbol_neighbour(i, j):
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if x < 0 or y < 0:
                continue
            try:
                if inputt[x][y] in symbols:
                    return True
            except IndexError:
                continue
    return False


def has_star_neighbour(i, j):
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if x < 0 or y < 0:
                continue
            try:
                if inputt[x][y] == "*":
                    return x, y
            except IndexError:
                continue
    return False


som_part_1 = 0
som_part_2 = 0

stars = {}
for i, line in enumerate(inputt):
    print("\n")

    # set for new line
    digit = ""
    touches_symbol = False
    touches_star = False

    for j, char in enumerate(line):
        if char == "." or char in symbols or char == "\n":
            if digit != "":
                # somm for part 1
                if touches_symbol:
                    som_part_1 += int(digit)

                # for part 2
                if touches_star:
                    try:
                        stars[star_position].append(digit)
                    except:
                        stars[star_position] = [digit]

            # reset
            digit = ""
            touches_symbol = False
            touches_star = False
            continue

        if char.isdigit():
            digit += char

            if has_symbol_neighbour(i, j):
                touches_symbol = True

            if has_star_neighbour(i, j):
                touches_star = True
                star_position = has_star_neighbour(i, j)

for key, value in stars.items():
    if len(value) == 2:
        a, b = value
        som_part_2 += int(a) * int(b)


print(som_part_2)

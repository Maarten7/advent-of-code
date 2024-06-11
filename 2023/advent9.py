def get_next(input):
    diffs = []
    for i in range(len(input) - 1):
        diffs.append(input[i + 1] - input[i])
    if all(map(lambda a: a == 0, diffs)):
        return input[-1]
    else:
        return get_next(diffs) + input[-1]


def get_first(input):
    diffs = []
    for i in range(len(input) - 1):
        diffs.append(input[i + 1] - input[i])
    if all(map(lambda a: a == 0, diffs)):
        return input[0]
    else:
        return input[0] - get_first(diffs)


som = 0
somm = 0
for line in open("advent9.txt"):
    line = list(map(int, line.split()))
    som += get_next(line)
    somm += get_first(line)

print(somm)

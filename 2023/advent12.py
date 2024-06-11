import re, math
import itertools
from functools import lru_cache


def is_valid(spring, counts):
    z = [len(x) for x in re.split("\.+", spring.strip("."))]
    return z == counts


def brute_force(input, counts):
    possibilities = 0
    marks = [m.start() for m in re.finditer("\?", input)]

    # hashtag nessesary
    required_hashtags = sum(counts) - input.count("#")

    impossible_group = "#" * (max(counts) + 1)

    for situ in itertools.product(["#", "."], repeat=input.count("?")):
        if situ.count("#") != required_hashtags:
            continue

        temp_line = input
        for mark, char in zip(marks, situ):
            # replace char
            temp_line = temp_line[:mark] + char + temp_line[mark + 1 :]

            if impossible_group in temp_line:
                break

        if is_valid(temp_line, counts):
            possibilities += 1
    return possibilities


@lru_cache(maxsize=10_000)
def is_ok(inputs, goal):
    if goal == len(goal) * "?":
        return True
    for in_char, goal_char in zip(inputs, goal):
        if goal_char == "?":
            continue
        if in_char != goal_char:
            return False
    return True


@lru_cache(maxsize=100_000)
def num_distributions(goal, counts):
    if goal == "":
        return 0

    m = len(goal)
    n = len(counts)

    first = counts[0]
    counts = counts[1:]
    dist = 0

    if n == 1:
        num = m - (first - 1)
        for z in range(num):
            last_part = z * "." + first * "#" + (m - z - first) * "."

            if not is_ok(last_part, goal):
                continue

            dist += 1

        return dist

    upper = m - (sum(counts) + (n - 1))
    for i in range(upper):
        first_part = i * "." + first * "#" + "."

        goal_head = goal[: len(first_part)]
        goal_tail = goal[len(first_part) :]

        if not is_ok(first_part, goal_head):
            continue

        dist += num_distributions(goal_tail, counts)
    return dist


som = 0
factor = 5
for i, l in enumerate(open("advent12.txt")):
    print(i)

    input, counts = l.strip().split(" ")
    counts = tuple(map(int, counts.split(",")))

    input = "?".join([input] * factor)
    counts = counts * factor

    som += num_distributions(input, counts)

print(som)

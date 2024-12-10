from heapq import heappush, heappop
import numpy as np



def main_1():
    input = np.array(
        [
            [int(i) for i in list(line.strip())]
            for line in open("advent171.txt", "r").readlines()
        ]
    )
    max_i, max_j = input.shape
    visited = set()
    path = []

    # (heatloss, position i, position j, direction, direction_count)
    start = (0, 0, 0, None, 0, [])
    heappush(path, start)

    while path:
        heat_loss, i, j, dir, dir_count, so_far = heappop(path)

        if (i, j, dir, dir_count) in visited:
            continue
        visited.add((i, j, dir, dir_count))

        if (i, j) == (max_i - 1, max_j - 1):
            break

        # 0 down, 1 up, 2 right, 3 left
        for new_dir, (new_i, new_j) in enumerate([(i+1, j), (i-1, j), (i, j+1), (i, j-1)]):

            # no more than 3 steps
            if dir == new_dir:
                if dir_count == 3:
                    continue
                else:
                    new_dir_count = dir_count + 1
            else:
                new_dir_count = 1

            # no outside grid
            if not (0 <= new_i < max_i and 0 <= new_j < max_j):
                continue

            # no 180 turn
            if set([dir, new_dir]) == set([1, 0]) or set([dir, new_dir]) == set([2, 3]):
                continue


            new_position = (
                heat_loss + input[new_i, new_j],
                new_i,
                new_j,
                new_dir,
                new_dir_count,
                so_far + [(i, j, dir, dir_count)]
            )
            heappush(path, new_position)

    print(heat_loss)

def main_2():
    input = np.array(
        [
            [int(i) for i in list(line.strip())]
            for line in open("advent171.txt", "r").readlines()
        ]
    )
    max_i, max_j = input.shape
    visited = set()
    path = []

    # (heatloss, position i, position j, direction, direction_count)
    start = (0, 0, 0, None, 0, [])
    heappush(path, start)

    while path:
        heat_loss, i, j, dir, dir_count, so_far = heappop(path)

        if (i, j, dir, dir_count) in visited:
            continue
        visited.add((i, j, dir, dir_count))

        if (i, j) == (max_i - 1, max_j - 1):
            break

        # 0 down, 1 up, 2 right, 3 left
        for new_dir, (new_i, new_j) in enumerate([(i+1, j), (i-1, j), (i, j+1), (i, j-1)]):

            # more than 4
            if dir != None and new_dir != dir and dir_count < 4:
                continue

            # no more than 10 steps
            if new_dir == dir:
                if dir_count == 10:
                    continue
                else:
                    new_dir_count = dir_count + 1
            else:
                new_dir_count = 1

            # no outside grid
            if not (0 <= new_i < max_i and 0 <= new_j < max_j):
                continue

            # no 180 turn
            if set([dir, new_dir]) == set([1, 0]) or set([dir, new_dir]) == set([2, 3]):
                continue


            new_position = (
                heat_loss + input[new_i, new_j],
                new_i,
                new_j,
                new_dir,
                new_dir_count,
                so_far + [(i, j, dir, dir_count)]
            )
            heappush(path, new_position)

    print(heat_loss)

    dir_str = {0:"v", 1:"^", 2:'>', 3:"<"}
    input = input.astype(str)
    for i, j, dir, dir_count in so_far:
        input[i, j] = dir_str.get(dir, ".")
    print(input) 

main_2()
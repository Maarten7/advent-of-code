import numpy as np
import os
import re
from pathlib import Path
import itertools


def main_1(file):
    input = open(file, "r").readline()
    input = [int(x) for x in input]
    max_id = int((len(input) - 1) / 2)
    counter = {int(des / 2): input[des] for des in range(0, len(input), 2)}

    check_sum = 0
    id = 0
    id_top = max_id
    index = 0
    for j in range(len(input)):

        inputj = input[j]

        if j % 2 == 0:
            for i in range(inputj):
                if counter[id] == 0:
                    continue
                check_sum += index * id
                index += 1
                counter[id] -= 1
            id += 1

        if j % 2 != 0:
            for i in range(inputj):
                try:
                    while counter[id_top] == 0:
                        id_top -= 1
                except KeyError:
                    return check_sum
                check_sum += index * id_top

                index += 1
                counter[id_top] -= 1


def main_2(file):
    input = open(file, "r").readline()
    input = [int(x) for x in input]

    cumsum = np.cumsum(input)
    counter = [[des, int(des / 2), input[des]] for des in range(0, len(input), 2)]
    spaces = [[des, 0, input[des]] for des in range(1, len(input), 2)]

    indices = []
    for i in range(len(cumsum)):
        if i == 0:
            start = 0
        else:
            start = cumsum[i - 1]
        indices.append(list(range(start, cumsum[i])))

    checksum = 0
    for j, id, count in counter[::-1]:

        for i in range(len(spaces)):
            j_position = spaces[i][0]
            space = spaces[i][2]

            if j < j_position:
                continue

            if count <= space:  
                for _ in range(count):
                    checksum += id * indices[j_position].pop(0)
                    spaces[i][2] -= 1
                break
            
        else:
            # NO SPACE FOUND
            # calculate part of checksum
            for _ in range(count):
                checksum += id * indices[j].pop(0)
    return checksum 



if __name__ == "__main__":
    advent_day = Path(os.path.basename(__file__)).stem

    file = f"test_input_{advent_day}.txt"
    test_1 = main_1(file)
    print(f"{test_1 = }")
    if test_1 == 1928:
        file = f"input_{advent_day}.txt"
        print(main_1(file))

    file = f"test_input_{advent_day}.txt"
    test_2 = main_2(file)
    print(test_2)
    if test_2 == 2858:
        file = f"input_{advent_day}.txt"
        print(main_2(file))

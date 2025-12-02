import numpy as np
import os
import re
import math
from pathlib import Path
import itertools
from sympy import divisors



def main_1(file):
    output = 0

    input = [el.split("-") for el in open(file, "r").readline().split(',')]
    input = [(int(e1), int(e2)) for [e1, e2] in input]

    for start, end in input:
        for id in range(start, end + 1):
            id = str(id)
            n = len(id)

            if n % 2 != 0:
                continue 

            fh, sh = id[0:n//2], id[n//2:]
            if fh == sh:
                output += int(id)
    return output

def main_2(file):
    output = 0

    input = [el.split("-") for el in open(file, "r").readline().split(',')]
    input = [(int(e1), int(e2)) for [e1, e2] in input]

    for start, end in input:
        for id in range(start, end + 1):
            invalid = False
            id = str(id)
            n = len(id)

            divisiorz = divisors(n)[1:]

            for divisor in divisiorz:
                digits = set()
                if invalid:
                    break
                for k in range(0, divisor):
                    part_size = n // divisor
                    part = id[(k * part_size):((k+1) * part_size)]
                    digits.add(part)

                if len(digits) == 1:
                    output += int(id)
                    invalid = True

    return output


if __name__ == "__main__":
    TEST_1_ANS = 1227775554 
    TEST_2_ANS = 4174379265 
    advent_day = Path(os.path.basename(__file__)).stem
    file = f"input_{advent_day}.txt"
    test_file = f"test_input_{advent_day}.txt"

    test_1 = main_1(test_file)
    print(f"{test_1 = }")
    if test_1 == TEST_1_ANS: 
        result_1 =  main_1(file)
        print(f"{result_1 = }")

    test_2 = main_2(test_file)
    print(f"{test_2 = }")
    if test_2 == TEST_2_ANS:
        result_2 =  main_2(file)
        print(f"{result_2 = }")

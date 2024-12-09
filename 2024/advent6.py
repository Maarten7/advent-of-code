from asyncio import sleep
import numpy as np
import os
import re
from pathlib import Path


class Arrow:
    def __init__(self, i, j, grid):
        self.i = i
        self.j = j
        self.direction = "up"
        self.grid = grid
        self.looping = False
    
    def rotate(self):
        rotate_rules = {"up": "rigth", "rigth": "down", "down": "left", "left": "up"}
        self.direction = rotate_rules[self.direction]
    
    def step(self):
        i, j = self.i, self.j
        match self.direction:
            case 'up':
                i = self.i - 1
            case "rigth":
                j = self.j + 1
            case "down":
                i = self.i + 1
            case "left":
                j = self.j - 1

        if self.grid[i, j] == str(self):
            self.looping = True
        
        if i < 0 or j < 0:
            raise IndexError

        if self.grid[i, j] == "#":
            self.rotate()
        else:
            self.i, self.j = i,j
    
    def location(self):
        return self.i, self.j
    
    def __str__(self):
        direction_symbol = {"up": "^", "rigth": ">", "down": "v", "left": "<"}
        direction = direction_symbol[self.direction]
        return direction

    def __repr__(self):
        direction_symbol = {"up": "^", "rigth": ">", "down": "v", "left": "<"}
        direction = direction_symbol[self.direction]
        return f"Arrow {self.i}, {self.j} {direction}"
    


def main_1(file):
    input = np.array([list(line) for line in np.loadtxt(file, dtype=str, comments="|")])
    arrow_i, arrow_j = np.where(input == "^")
    num_obs_start = len(np.where(input == "#")[0])  
    arrow = Arrow(arrow_i[0], arrow_j[0], input)

    try:
        while True:
            input[arrow.location()] = "X" 
            arrow.step()
            #input[arrow.location()] = str(arrow)
            #print(np.array(["".join(inz) for inz in input]))
            #sleep(.05)
            #os.system('clear')
    except IndexError:
        ans = len(np.where(input == "X")[0])
        return ans 


def main_2(file):
    empty_input = np.array([list(line) for line in np.loadtxt(file, dtype=str, comments="|")])
    arrow_i, arrow_j = np.where(empty_input == "^")
    arrow = Arrow(arrow_i[0], arrow_j[0], empty_input)

    try:
        input = empty_input.copy()
        while True:
            input[arrow.location()] = "X" 
            arrow.step()
    except IndexError:
        possible_obstructions = np.where(input == "X")

    looping_count = 0
    for xi, xj in np.transpose(possible_obstructions):
        input = empty_input.copy()
        count_input = np.zeros(empty_input.copy().shape)
        input[xi, xj] = "#"
        arrow = Arrow(arrow_i[0], arrow_j[0], input)
        try:
            while not arrow.looping:
                input[arrow.location()] = str(arrow)

                count_input[arrow.location()] += 1

                if count_input[arrow.location()] > 3:
                    arrow.looping = True

                arrow.step()
            looping_count += 1 
            #print(xi, xj, arrow.looping)

        except IndexError:
            continue

    return looping_count



if __name__ == "__main__":
    advent_day = Path(os.path.basename(__file__)).stem

    file = f"test_input_{advent_day}.txt"
    test_1 = main_1(file)
    print(test_1)
    if test_1 == 41:
        file = f"input_{advent_day}.txt"
        print(main_1(file))

    file = f"test_input_{advent_day}.txt"
    test_2 = main_2(file)
    print(test_2)
    if test_2 == 6:
        file = f"input_{advent_day}.txt"
        print(main_2(file))

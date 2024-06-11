import unittest
from math import sqrt, floor, ceil

def first_bigger_uneven_square(number):
    root = sqrt(number)
    ceil_root = ceil(root) 
    
    if ceil_root ** 2 % 2 == 0:
        ceil_root += 1

    return ceil_root ** 2

def first_smaller_uneven_square(number):
    root = sqrt(number)
    ceil_root = floor(root) 
    
    if ceil_root ** 2 % 2 == 0:
        ceil_root += 1

    return ceil_root ** 2

def ring(number):
    """ returns the ring a certain number is in"""
    uneven_square = first_bigger_uneven_square(number)
    assert uneven_square % 2 != 0
    assert int(sqrt(uneven_square) + 0.5) ** 2 == uneven_square

    ring = sqrt(uneven_square) / 2 
    return ring - 0.5

def length_side(ring):
    return ring * 2 + 1

def corners(number):
    """returns corners of a certain number
        including last corner of last ring
        5 corners"""
    corner = first_bigger_uneven_square(number)
    small_corner = first_smaller_uneven_square(number)

    ringg = ring(number)
    side = length_side(ringg)
    
    length_to_corner = ringg * 2
    steps_to_corner = corner - number
    
    corners = [small_corner] + [corner - (side - 1) * i for i in range(4)]
    return corners

def manhattan_distance_spiral(number):

    cornerz = corners(number)
    steps_to_corner = [abs(number - i) for i in cornerz]
    return ring(number) * 2 - min(steps_to_corner)

def start_coordinate(ring):
    x = ring

    if ring == 0 or ring == 1:
        y = 0
    else:
        y = ring * -1 + 1

    return x,y

def urlam_spiral_cordinates(ring=0, end=3):

    while True:

        x, y = start_coordinate(ring)
        side = length_side(ring)

        yield x, y

        for i in range(1, side - 1):
            x, y = x, y + 1
            yield x, y

        for i in range(1, side):
            x, y = x - 1, y
            yield x, y

        for i in range(1, side):
            x, y = x, y - 1
            yield x, y

        for i in range(1, side):
            x, y = x + 1, y
            yield x, y

        ring += 1 
        if end and ring > end:
            break

def urlam_sum():
    summ_spiral = {(0,0): 1}

    for c in urlam_spiral_cordinates(1, None):
        x,y = c 
        ring = [
            (x+1, y), 
            (x+1, y+1),
            (x  , y+1),
            (x-1, y+1),
            (x-1, y),
            (x-1, y-1),
            (x  , y-1),
            (x+1, y-1),
        ]
        summ = 0
        for adjesent in ring:
            try:
                summ += summ_spiral[adjesent]
            except KeyError:
                summ += 0

        summ_spiral[c] = summ

        if summ > 277678:
            return summ


class Test(unittest.TestCase):

    def test_example(self):
        self.assertEqual(manhattan_distance_spiral(1), 0)  
    def test_example2(self):
        self.assertEqual(manhattan_distance_spiral(12), 3)  
    def test_example3(self):
        self.assertEqual(manhattan_distance_spiral(23), 2)  
    def test_example4(self):
        self.assertEqual(manhattan_distance_spiral(1024), 31)  
    def test_example5(self):
        self.assertEqual(manhattan_distance_spiral(26), 5)  
    def test_example6(self):
        self.assertEqual(manhattan_distance_spiral(27), 4)  
    def test_example7(self):
        self.assertEqual(manhattan_distance_spiral(28), 3)  

    def test_square(self):
        self.assertEqual(manhattan_distance_spiral(81), 8)  
    def test_square2(self):
        self.assertEqual(manhattan_distance_spiral(25), 4)  

    def test_coordinates(self):
        self.assertEqual(start_coordinate(0), (0,0))
    def test_coordinates1(self):
        self.assertEqual(start_coordinate(1), (1,0))
    def test_coordinates2(self):
        self.assertEqual(start_coordinate(2), (2,-1))

if __name__ == '__main__':
    unittest.main(exit=False)
    print(manhattan_distance_spiral(277678))

import matplotlib.pyplot as plt
plt.plot([manhattan_distance_spiral(i) for i in range(10000)])
plt.show()


import unittest

def captha(input_string):
    summ  = 0
    for i in range(len(input_string)):
        prev = input_string[i-1]
        item = input_string[i] 
        if prev == item:
            summ += int(prev)

    return summ

def captha2(input_string):
    summ  = 0
    half_way = len(input_string) / 2

    for i in range(len(input_string)):
        prev = input_string[i-half_way]
        item = input_string[i] 
        if prev == item:
            summ += int(prev)

    return summ

class TestCaptha(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(captha("1122"), 3)  
    def test_example_2(self):
        self.assertEqual(captha("1111"), 4)  
    def test_example_3(self):
        self.assertEqual(captha("1234"), 0)  
    def test_example_4(self):
        self.assertEqual(captha("91212129"), 9)


class TestCaptha2(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(captha2("1212"), 6)  
    def test_example_2(self):
        self.assertEqual(captha2("1221"), 0)  
    def test_example_3(self):
        self.assertEqual(captha2("123425"), 4)  
    def test_example_4(self):
        self.assertEqual(captha2("123123"), 12)  
    def test_example_4(self):
        self.assertEqual(captha2("12131415"), 4)

if __name__ == '__main__':
    unittest.main(exit=False)
    input_string = open("input.txt").read().rstrip()
    print(captha(input_string))
    print(captha2(input_string))

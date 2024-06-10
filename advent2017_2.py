import unittest

def check_sum(input_string):
    summ = 0
    input_string = input_string.rstrip().split("\n")

    for row in input_string:
        row = row.rstrip().split('\t')
        row = list(map(int, row))

        summ += max(row) - min(row)

    return summ 

def sum_evenly_divisible_values(input_string):
    summ = 0
    input_string = input_string.rstrip().split("\n")

    
    for row in input_string:
        row = row.rstrip().split('\t')
        row = list(map(int, row))

        for i in range(len(row)):
            for j in range(i, len(row)):
                ri = row[i]
                rj = row[j]
                mod = max(ri, rj) % min(ri, rj)
                if mod == 0 and ri != rj:
                    summ += max(ri, rj) / min(ri, rj)
    return summ


class TestCheckSum(unittest.TestCase):

    def test_example(self):
        self.assertEqual(check_sum("5\t1\t9\t5\n7\t5\t3\t3\n2\t4\t6\t8\n"), 18)  

    def test_example2(self):
        self.assertEqual(sum_evenly_divisible_values("5\t9\t2\t8\n9\t4\t7\t3\n3\t8\t6\t5\n"), 9)  
        
if __name__ == '__main__':
    unittest.main(exit=False)
    input_string = open("input.txt").read()
    print(check_sum(input_string))
    print(sum_evenly_divisible_values(input_string))

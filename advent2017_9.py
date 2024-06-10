import unittest
import re

def num_groups_and_score(ins, brackets=('{', '}')):

    open_groups = 0
    closed_groups = 0
    score = 0

    for char in ins:
        if char == brackets[0]:
            open_groups += 1
        if char == brackets[1]:
            score += open_groups
            open_groups -= 1
            closed_groups += 1

    return closed_groups, score 

def score_and_garbage_count(ins):
    #remove ! and traling char
    ins = re.sub(r'!.', '', ins)
    len_a = len(ins)
   
    # count garbage groups
    garbage_groups, _ = num_groups_and_score(ins, brackets=('<','>'))

    #remove garbage
    ins = re.sub(r'<.*?>', '', ins)
    len_b = len(ins)

    garbage_count = len_a - len_b - garbage_groups * 2
    _, score = num_groups_and_score(ins)
    return score, garbage_count


if __name__ == '__main__':
    print(score_and_garbage_count(open('input_9.txt').read()))

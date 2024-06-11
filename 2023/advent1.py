import regex as re

f = open("advent.txt")
digits = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
spelled_out_digits = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
re_digits = "|".join(digits + spelled_out_digits)


def to_digit(digit):
    if len(digit) == 1:
        return digit
    else:
        return str(spelled_out_digits.index(digit) + 1)


somm = 0
for line in f:
    print(line)
    matches = list(re.finditer(re_digits, line, overlapped=True))
    first_match = matches[0].group()
    last_match = matches[-1].group()
    combi = int(to_digit(first_match) + to_digit(last_match))
    somm += combi
print(somm)

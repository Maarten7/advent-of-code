
def has_adjacent_digits(number):
    number = str(number)

    for i, char in enumerate(number[:-1]):
        if char == number[i+1]:
            return True
    return False

def has_no_decreasing_digits(number):
    number = str(number)
    for i, char in enumerate(number[:-1]):
        if int(char) > int(number[i+1]):
            return False
    return True

def has_two_adjacent(number):
    number = str(number)

    for char in number:
        if number.count(char) == 2:
            return True
    return False



def is_password(number):
    if has_adjacent_digits(number):
        if has_no_decreasing_digits(number):
            if has_two_adjacent(number):
                return True
    return False

summ = 0
for i in range(278384, 824795):

    if is_password(i):
        summ += 1

print(summ)

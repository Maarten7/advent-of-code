from collections import OrderedDict


def hash(input):
    current_value = 0

    for char in input:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


def hashmap(input, book):
    if "-" in input:
        label = input[:-1]
        box = hash(label)
        # remove lens in box if present. move remaining lensen forward
        book[box].pop(label, None)

    if "=" in input:
        # replace or add lens
        label, focal_length = input.split("=")
        box = hash(label)
        book[box][label] = int(focal_length)

    return book


input = ""
for line in open("advent15.txt"):
    input += line.strip()
# input = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
input = input.split(",")

book = OrderedDict({i: {} for i in range(256)})
som = 0
somm = 0
for inn in input:
    som += hash(inn)
    book = hashmap(inn, book)

for box, lenses in book.items():
    for i, (key, focal_length) in enumerate(lenses.items()):
        z = (box + 1) * (i + 1) * focal_length
        somm += z

print(som)
print(somm)

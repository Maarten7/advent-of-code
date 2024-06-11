import math


class Day8:
    def __init__(self, input_file):
        with open(input_file) as f:
            instructions = f.readline()
            self.instructions = str(instructions).strip("\n")
            next(f)

            self.mapping = {}
            for line in f:
                node, labels = line.split("=")
                labels = labels.strip("\n ()").split(",")
                labels = list(map(str.strip, labels))
                self.mapping[node.strip()] = labels

    def get_steps(self, node):
        step = 1
        # while node != "ZZZ":
        while node[2] != "Z":
            instruction = self.instructions[(step - 1) % len(self.instructions)]
            if instruction == "R":
                node = self.mapping[node][1]
            if instruction == "L":
                node = self.mapping[node][0]
            step += 1

        return step - 1

    def part_one(self):
        node = "AAA"
        return self.get_steps(node)

    def part_two(self):
        nodes = [node for node in self.mapping.keys() if node[2] == "A"]
        steps = [self.get_steps(node) for node in nodes]
        return math.lcm(*steps)


print(Day8("advent8.txt").part_one())
print(Day8("advent8.txt").part_two())

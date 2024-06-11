class Game:
    max_cubes = {"red": 12, "green": 13, "blue": 14}

    def __init__(self, game_id):
        self.id = game_id
        self.cubes = {"red": 0, "green": 0, "blue": 0}


somm = 0
for line in open("advent2.txt"):
    print(line)
    game_id, game_dices = line.split(":")
    sets = game_dices.split(";")

    game_id = int(game_id[4:])
    game = Game(game_id)

    by_color = {"red": [], "green": [], "blue": []}
    for set in sets:
        cubes = set.split(",")
        for cube in cubes:
            amount, color = cube.strip().split(" ")
            amount = int(amount)

            by_color[color].append(amount)
    somm += max(by_color["red"]) * max(by_color["green"]) * max(by_color["blue"])
print(somm)

somm = 0

won_games = {game_id: 1 for game_id in range(1, 202)}
for line in open("advent4.txt"):
    game, numbers = line.split(":")
    game = game.split()[-1]
    game = int(game)

    winning, begotten = numbers.split("|")

    winning = winning.strip().split()
    begotten = begotten.strip().split()
    winning = set(map(int, winning))
    begotten = set(map(int, begotten))

    points = len(winning.intersection(begotten))
    if points > 0:
        somm += 2 ** (points - 1)

        for i in range(game + 1, game + points + 1):
            won_games[i] += won_games[game]

print(somm)
print(won_games)
print(sum(won_games.values()))

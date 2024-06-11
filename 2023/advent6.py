f = open("advent6.txt")

times = list(map(int, next(f).split(":")[1].strip().split()))
distances = list(map(int, next(f).split(":")[1].strip().split()))

for i, time in enumerate(times):
    # print(time)

    over_record = 0
    for t in range(time):
        if t * (time - t) > distances[i]:
            over_record += 1

    print(over_record)

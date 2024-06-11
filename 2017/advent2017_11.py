combos = [
        ('n', 's', None), 
        ('ne', 'sw', None), ('nw', 'se', None),
        ('n', 'se', 'ne'), ('n', 'sw', 'nw'),
        ('s', 'ne', 'se'), ('s', 'nw', 'sw'),
        ('ne', 'nw', 'n'), ('se', 'sw', 's'),
]



steps = open('input_11.txt').read().strip().split(',')


def distance_from_start(input_steps):
    steps = input_steps.copy()
    reducing = True 
    for a, b, r in combos:
        while a in steps and b in steps:
            steps.remove(a)
            steps.remove(b)
            if r:
                steps.append(r)

    return len(steps)

dis = distance_from_start(steps))
print(dis)

lens = len(steps)
maxx = dis 
for i in range(lens):
    dis = distance_from_start(steps[:lens - i])

    if dis > maxx:
        maxx = dis

print(maxx)

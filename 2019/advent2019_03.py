import matplotlib.pyplot as plt

def wire_to_path(wire):
    x,y = 0,0
    path = [(x,y)]
    step = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    for ins in wire:
        direction = ins[0]
        steps = int(ins[1:])
        
        for _ in range(steps):
            dx, dy = step[direction] 
            x += dx
            y += dy
            path.append((x,y))
    return path

def intersections(path_a, path_b):
    set_a = set(path_a)
    set_b = set(path_b)
    return [point for point in set_a if point in set_b]

def min_intersection(path_a, path_b):
    manhattan = [abs(x) + abs(y) for x, y in intersections(path_a, path_b)]
    manhattan.remove(0)
    return min(manhattan)

def shortes_time(path_a, path_b):
    times = [path_a.index(i) + path_b.index(i) for i in intersections(path_a, path_b)]
    times.remove(0)
    return min(times)

wire_a, wire_b = open('input_03.txt')

wire_a = wire_a.rstrip().split(',')
wire_b = wire_b.rstrip().split(',')

path_a = wire_to_path(wire_a)
path_b = wire_to_path(wire_b)

print(min_intersection(path_a, path_b))
print(shortes_time(path_a, path_b))

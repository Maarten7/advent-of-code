def get_data(): 
    offsets = open('input_5.txt').read().split('\n')[:-1]
    for i, o in enumerate(offsets):
        offsets[i] = int(o)
    return offsets

def counter(data, part2=False):
    i = 0
    step = 0

    while i < len(data):
        instruction = data[i]
        
        if not part2:
            data[i] += 1
        else:
            if instruction >= 3:
                data[i] -= 1
            else:
                data[i] += 1

        i += instruction

        step += 1
    return step


print(counter(get_data()))
print(counter(get_data(), True))

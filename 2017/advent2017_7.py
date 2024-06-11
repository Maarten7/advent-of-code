def get_data():
    data = open('input_7.txt')
    for line in data: 
        info = line.replace(',', '').strip().split(' ')

        name = info[0]
        weight = int(info[1].strip('(').strip(')'))

        if len(info) > 2:
            childs = info[3:]
        else: 
            childs = None

        yield name, weight, childs

def find_first():
    carriers = set()
    carried  = set() 
    for name, _, childs in get_data():
        
        if childs:
            carriers.add(name)
            carried.update(childs)
       
    return carriers.difference(carried).pop()

first = find_first()

print(first)

weights = {}
for name, weight, childs in get_data():
    weights[name] = weight

children = {}
for name, weight, childs in get_data():
    children[name] = childs 

full_weights = {} 
def get_weight(name):
    
    summ = weights[name]
    kids = children[name]

    if kids:
        child_weights = []
        for child in kids:
            weight = get_weight(child)
            child_weights.append(weight)

            summ += weight

    full_weights[name] = summ
    return summ

get_weight(first)

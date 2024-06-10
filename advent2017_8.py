
def get_data():
    for line in open('input_8.txt'):

        line = line.split(' ')
        
        register = line[0]
        instuction = line[1]
        amount = int(line[2])

        check_register = line[4]
        check = line[5] 
        check_amount = int(line[6])

        yield register, instuction, amount, check_register, check, check_amount


registers = {}


maxx = 0
for register, instuction, amount, check_register, check, check_amount in get_data():
    if instuction == 'inc':
        ins = +1
    else:
        ins = -1

    try:
        cr = registers[check_register]
    except KeyError:
        cr = 0
    try:
        registers[register]
    except KeyError:
        registers[register] = 0


    if check == '<':
        val = cr < check_amount
    if check == '>':
        val = cr > check_amount
    if check == '>=':
        val = cr >= check_amount
    if check == '<=':
        val = cr <= check_amount
    if check == '!=':
        val = cr != check_amount
    if check == '==':
        val = cr == check_amount

    if val:
        registers[register] += ins * amount 
    
    if registers[register] > maxx:
        maxx = registers[register]


key = max(registers, key=registers.get)
print(registers[key])
print(maxx)

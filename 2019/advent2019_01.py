from math import floor

modules = open('input_01.txt')

def get_fuel(mass, summ=0):
    fuel = floor(mass/ 3.) - 2
    if fuel <= 0:
        return summ
    else:
        return get_fuel(fuel, summ + fuel) 

summ1, summ2 = 0, 0
for module in modules:
    mass = int(module)

    fuel = floor(mass / 3.) - 2

    summ1 += fuel
    summ2 += get_fuel(mass)

print(summ2)

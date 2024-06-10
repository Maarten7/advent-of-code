def run(prog, noun, verb):
   
    program = prog[:]
    i = 0

    program[1] = noun 
    program[2] = verb 

    while True:

        opp_code = program[i]

        if opp_code == 99:
            break

        in_1 = program[program[i + 1]]
        in_2 = program[program[i + 2]]
        out = program[i + 3]

        if opp_code == 1:
           out = in_1 + in_2 

        elif opp_code == 2:
            out = in_1 * in_2


        program[program[i + 3]] = out
        i += 4

    return program[0]

def finder(prog):
    for noun in range(0,100):
        for verb in range(0,100):
            output = run(prog, noun, verb)

            if output == 19690720:
                return noun, verb


prog = open('input_02.txt').read().rstrip().split(',')
prog = [int(x) for x in prog]
noun, verb = finder(prog)
print(100 * noun + verb)

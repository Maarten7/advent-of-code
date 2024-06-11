def run(prog, noun, verb):
   
    program = prog[:]
    i = 0

    program[1] = noun 
    program[2] = verb 

    while True:
        mode_1, mode_2, mode_3, mode_4 = 0, 0, 0, 0 

        opp_code = str(program[i])[-2:]
        encoding = str(program[i])[:-2]

        if opp_code == 99:
            break

        mode_1 = encoding[-1]
        mode_2 = encoding[-2]
        mode_3 = encoding[-3]
        mode_4 = encoding[-4]

        if mode_1 == 0:
            in_1 = program[program[i + 1]]
        elif mode_1 == 1:
            in_1 = program[i + 1]
        if mode_2 == 0:
            in_2 = program[program[i + 1]]
        elif mode_2 == 1:
            in_2 = program[i + 1]

        if opp_code == 1:
            out = in_1 + in_2 
        elif opp_code == 2:
            out = in_1 * in_2

        if mode_3 == 0:
            program[program[i + 3]] = out
        if mode_3 == 1:
            program[i + 3] = out

        elif opp_code == 3:
            program[in_1]


        program[program[i + 3]] = out
        i += 4

    return program[0]


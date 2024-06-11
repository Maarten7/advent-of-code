def get_data():
    data = open('input_6.txt').read().strip().split('\t')
    return [int(i) for i in data] 

def redistribute(state):
    
    # determine memory bank with most blocks
    max_blocks = max(state)
    i = state.index(max_blocks)

    # take all blocks from bank
    state[i] = 0

    # redistribute blocks
    for j in range(max_blocks):
        try:
            state[i + 1] += 1
            i += 1
        except IndexError:
            i = 0 
            state[i] += 1 

    return state

def redistribution_cycles(state):
    states = []
    count = 0

    while state not in states:

        states.append(state.copy())
        state = redistribute(state)
        count += 1

    loop_lenght = count - states.index(state) 
    return count, loop_lenght


print(redistribution_cycles([0, 2, 7, 0]))
print(redistribution_cycles(get_data()))

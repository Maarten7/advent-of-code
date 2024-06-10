import numpy as np
import operator
import functools

def fold(lengths, circular, skip_size=0, i=0):
    for j in lengths:
       
        slic = np.take(circular, range(i, i + j), mode='wrap')
        np.put(circular, range(i, i + j), np.flip(slic), mode='wrap')

        i += j + skip_size
        skip_size += 1

    return circular, skip_size, i

def fold_n_times(n, ins, size):
    skip_size, i = 0, 0
    circular = np.arange(size)
    for _ in range(n):
        circular, skip_size, i = fold(ins, circular, skip_size, i)
    return circular 

def dense_hash(sparse):
    dense = []
    for i in range(0, 256, 16):
        d = functools.reduce(operator.xor, sparse[i: i + 16])
        dense.append(d)
    dense = ['{:02x}'.format(e) for e in dense]
    return ''.join(dense)

def knot_hash(ins):
    inasci = [ord(x) for x in ins]
    suffix = [17, 31, 73, 47, 23]
    inasci += suffix

    sparse = fold_n_times(64, inasci, 256)
    dense = dense_hash(sparse)
    return dense

# part 1
ins = open('input_10.txt').read().strip().split(',')
intin = [int(x) for x in ins]
intin, _, _ = fold(intin, np.arange(256))
print(intin[0] * intin[1])

# part 2 
ins = open('input_10.txt').read().strip()
print(knot_hash(ins))

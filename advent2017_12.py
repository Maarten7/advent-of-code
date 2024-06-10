def find_group(num):
    null_set = set() 
    condition = True
    while condition: 

        pipes = open('input_12.txt')
        len_set = len(null_set)

        for line in pipes:
            line = line.strip().split(' ')

            home = int(line[0])
            connect = line[2:]

            if home == num:
                for c in connect:
                    null_set.add(int(c.strip(',')))

            for c in connect:
                if int(c.strip(',')) in null_set:
                    null_set.add(home)
            
        pipes.close()
        if len(null_set) == len_set:
            condition = False
                
        
    return null_set

groups = [find_group(0)]

pipes = open('input_12.txt')
for line in pipes:
    line = line.strip().split(' ')

    home = int(line[0])
    connect = line[2:]
    
    in_group = False
    for group in groups:
        if home in group:
            in_group = True 
   
    if not in_group:
       groups.append(find_group(home))

print(len(groups))

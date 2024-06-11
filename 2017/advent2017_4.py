
def no_same_words():
    phrases = open('input_4.txt')
    summ = 0
    for line in phrases:
        valid = True
        line = line.strip().split(' ')
        for i, word in enumerate(line): 
            if word in line[i+1:]:
                valid = False 
                break

        if valid:
            summ += 1

    return summ

def anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    if set(word1) != set(word2):
        return False
    
    word2 = list(word2)
    for i, letter in enumerate(word1):
        if letter in word2:
            j = word2.index(letter)
            word2.pop(j)
        else:
            return False
    return True

def no_anagram():
    phrases = open('input_4.txt')
    summ = 0
    for line in phrases:
        valid = True
        line = line.strip().split(' ')
        for i, word1 in enumerate(line): 
            for j, word2 in enumerate(line):
                if i==j:
                    continue

                if anagram(word1, word2):
                    valid = False
                    break
            if not valid:
                break

        if valid:
            summ += 1

    return summ

print(anagram('hoimaarten', 'maartenioh'))
print(no_anagram())

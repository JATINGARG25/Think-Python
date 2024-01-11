def is_three_consecutive(word):

    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            count = 0
            i = i + 1
    return False


def find_triple_double():
    fin = open('word.txt')
    for line in fin:
        word = line.strip()
        if is_three_consecutive(word):
            print(word)

find_triple_double()
with open('word.txt') as fd:
    word_list = fd.read().split()
    word_list.sort()

def bisect(liist,word):
    original = liist
    while True:
        middle = int(len(liist) / 2)
        if word > liist[middle]:
            liist = liist[middle:]
        elif word < liist[middle]:
            liist = liist[:middle]
        elif word == liist[middle]:
            return original.index(word)

        if len(liist) == 1:
            if word != liist[:]:
                return None
            else:
                return original.index(word)

print(bisect(word_list,"suppose"))

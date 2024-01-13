fd = open("word.txt")

def dictionary():
    word_dict = dict()
    for line in fd:
        word = line.strip()
        word_dict[word] = word
    return word_dict

print(dictionary())
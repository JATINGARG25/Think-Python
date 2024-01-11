def find(word, letter,index):

    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return "letter is not present in the given word."

print(find("banana","a",4))
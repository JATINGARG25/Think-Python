def has_no_e(word,forbidden):
    # fin = open(s)
    # word = fin.readline()

    if not forbidden in word:
        return word
    else:
        return -1 

forbidden = input("Enter an alphabet : ")
print(has_no_e("word.txt kaise hai",forbidden))


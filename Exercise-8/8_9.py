def rotate_letter(a, n): # here a is a single alphabat
    
    if a.isupper():
        start = ord('A')
    elif a.islower():
        start = ord('a')
    else:
        return a

    c = ord(a) - start
    i = (c + n) % 26 + start
    return chr(i)

def rotate_word(word, n):

    rw = ''
    for a in word:
        rw += rotate_letter(a, n)
    return rw

print(rotate_word("abba",3))

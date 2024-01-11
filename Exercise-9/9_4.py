def uses_only(word,string):
    for letter in word:
        if letter not in string:
            return False
    return True

print(uses_only("abcdabcdab","abcd"))
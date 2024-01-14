from string import *

with open("word.txt") as fd:
    words = fd.read().strip()

# print(punctuation)
print(words)
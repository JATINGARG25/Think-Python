with open('word.txt') as fd:
    words = fd.read().split()

def method_one(words):
    wordList = []
    for line in words:
        line = line.strip()
        wordList.append(line)
    print(len(wordList))
    print(wordList[:10])

def method_two(words):
    wordList = []
    for line in words:
        line = line.strip()
        wordList += [line]
    print(len(wordList))
    print(wordList[:10])

method_two(words)
method_one(words)

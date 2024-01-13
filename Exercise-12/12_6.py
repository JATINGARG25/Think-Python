# dict = {'a':1,'b':2}
# t = dict.items()
# print(t)

def sort_by_length(word):
    t = []
    for word in words:
        t.append((len(word), word))
        t.sort(reverse=True)

    res = []
    for length, word in t:
        res.append(word)
    return res

words = ["jatin","sumit","akash","veer","alok","atul","dhruv","rohit"]

print(sort_by_length(words))

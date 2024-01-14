import random

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0) + 1
    return d

def coose_form_hist(histogram):
        l = []
        for key, value in histogram.items():   
                l.extend([key] * value) #word needs to be inside a list
        return random.choice(l)

list = ["a","a","d","c"]
a = histogram(list)
print(coose_form_hist(a))
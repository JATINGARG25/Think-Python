def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0) + 1
    return d

def reverse_lookup(d, v):
    list_of_k = []
    for k in d:
        if d[k] == v:
            list_of_k.append(k)
    return list_of_k

h = histogram("abcdefgabstoyhgjnfvbskhf")
k = (reverse_lookup(h,3))

print(h)
print(k)

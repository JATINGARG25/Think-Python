def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0) + 1
    return d

def print_histogram(h):
    key_list = sorted(h.keys())
    for k in key_list:
        print(k,h[k])

h = histogram("abcdefgabstoyhgjnfvbskhf")
print_histogram(h)
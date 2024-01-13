
def has_duplicate(s):

    d = {}
    for val in s:
        if val in d:
            return True
        d[val] = val
    return False

list = [1,2,3]

print(has_duplicate(list))

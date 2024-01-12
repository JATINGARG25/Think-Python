def duplicate_remove(l):
    for element in l:
        if l.count(element) > 1:
            l.remove(element)
            
    return l

a = [1,2,3,4,5,6,7,8,9,0,1,2,3]
print(duplicate_remove(a))
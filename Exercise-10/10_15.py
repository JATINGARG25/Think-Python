def has_duplicate(l):
    for element in l:
        if l.count(element) > 1:
            return True
    
    return False

a = [1,2,3,4,5,6,7,8,9,0,1]
print(has_duplicate(a))
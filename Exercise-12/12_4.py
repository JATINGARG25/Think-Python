# # zip function

# a = 'jatin'
# b = [1,2,3,4,5]

# print(zip(a,b))

def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False

print(has_match((1,2,3,4,5,6,7,8,9,10),(1,2,3,4,5,6,7,3,2,3,2,3)))
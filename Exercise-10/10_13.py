def is_sorted(l):

    for i in range(len(l)-1):

        if l[i] > l[i+1]:
            return False
    return True

a = [1,2,3,3,5]

print(is_sorted(a))
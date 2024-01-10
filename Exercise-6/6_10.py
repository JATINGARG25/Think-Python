def is_power(a,b):
    c = b**(a/b)
    if a%c== 0:
        return True
    else:
        return False

print(is_power(4,2))
import math

def compare(x,y):
    if x>y:
        return 1
    elif x==y:
        return 0
    else:
        return -1

x = int(input("Enter the value of x : "))
y = int(input("Enter the value of y : "))

print(compare(x,y))



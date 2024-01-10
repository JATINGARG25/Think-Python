# import math

# def distance(x1,y1,x2,y2):
#     dx = (x2-x1)**2
#     dy = (y2-y1)**2

#     result = math.sqrt(dx+dy)
#     return result

# print(distance(1,2,4,6))

import math

def hypotenuse(len1,len2):

    p = (len1)**2
    b = (len2)**2

    length = math.sqrt(p+b)
    return length

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))

print(f"Length of hypotenuse is {hypotenuse(a,b)}")

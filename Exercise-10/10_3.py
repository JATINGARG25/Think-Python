# addition and multiplication operator on lists

a = [1,2,3]
b = [3,4,5,6]

c = a+b
print(c)
print(a*3)

# slice operator on the list

print(b[1:3])
print(b[1:])
print(b[:3])
print(b[:])

# slice operator also used in the updation of elements

a[1:3] = ["x","y"]
print(a)
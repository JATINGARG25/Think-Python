a = "banana"
b = "banana"

print(a is b)  # it is true because string make the same object

l1 = [1,2,3]
l2 = [1,2,3]  

# it is false because list do not make the same object
print(l1 is l2) 

# form the above discussion we can say that if two objects are identical,
# they are also equivalent, but if they are equivalent, they are not necessarily identical.

c = [1,2,3]
d = c           # this concept is called aliasing

# print(c is d) # it is true because now c and d have the same object
d[0] = 2526
print(c)
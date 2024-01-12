# to convert a string into list -- using in-built function list 

s = "jatin"
l = list(s)
print(l)

s1 = "jatin is a very goodboy"
l1 = s1.split()
print(l1)

s2 = "jatin*is*a*verygood*boy and*also*good in english"
star = "*"
l2 = s2.split(star)
print(l2)

# to join a string

l3 = ['jatin', 'is', 'a', 'verygood', 'boy and', 'good in english']
space = " "
s3 = space.join(l3)
print(s3)
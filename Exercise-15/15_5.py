import copy

class Point(object):
    pass

def print_point(p):
    print("(%f %f)" % (p.x,p.y))

p1 = Point()
p1.x = 5
p1.y = 65

p2 = copy.copy(p1)

print(p1.x,p1.y)
print(p2.x,p2.y)

print(p1 is p2)
print(p1 == p2)

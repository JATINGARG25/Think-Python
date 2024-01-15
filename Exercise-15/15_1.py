class Point(object):
    pass

def print_point(p):
    print("(%f %f)" % (p.x,p.y))

def distance_between_point(p,q):
    a = (p-q)
    print(a)

blank = Point()
blank.x = 3.0
blank.y = 4.0

distance_between_point(blank.x,blank.y)
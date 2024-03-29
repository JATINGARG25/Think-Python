class Point(object):
    pass

class Rectangles(object):
    pass

def print_point(p):
    print("(%f , %f)" % (p.x,p.y))

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0

    return p

box = Rectangles()

box.width = 100.0
box.height = 300.0

box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

centre = find_center(box)
print_point(centre)


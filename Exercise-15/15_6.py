import copy

class Point(object):
    pass

class Rectangles(object):
    pass

def print_point(p):
    print("(%f , %f)" % (p.x,p.y))

def move_rectangle(rect,dx,dy):
    rect.corner.x += dx
    rect.corner.y += dy

def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight

box = Rectangles()

box.width = 100.0
box.height = 300.0

box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

box2 = copy.copy(box)

print(box.width,box.height)
print(box2.width,box2.height,box2.corner.x)





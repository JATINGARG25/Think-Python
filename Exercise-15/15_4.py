class Point(object):
    pass

class Rectangles(object):
    pass

def print_point(p):
    print("(%f , %f)" % (p.x,p.y))

def move_rectangle(rect,dx,dy):
    rect.corner.x += dx
    rect.corner.y += dy

box = Rectangles()

box.width = 100.0
box.height = 300.0

box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

print(box.corner.x , box.corner.y)
move_rectangle(box,5,65)
print(box.corner.x , box.corner.y)





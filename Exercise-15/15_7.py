import copy

class Point(object):
    pass

class Rectangles(object):
    pass

def move_rectangle(rect):
    rect2 = copy.deepcopy(rect)
    return rect2

box = Rectangles()

box.width = 100.0
box.height = 300.0

box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

new_box = move_rectangle(box)

print(new_box.corner.x)

print(new_box.corner is box.corner)
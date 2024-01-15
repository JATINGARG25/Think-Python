# objects are mutuable

class Rectangles(object):
    pass

def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight

box = Rectangles()
box.width = 100.0
box.height = 300.0

print(box.width,box.height)

grow_rectangle(box,100,200)        # in this way we can change the values of the object

print(box.width,box.height)






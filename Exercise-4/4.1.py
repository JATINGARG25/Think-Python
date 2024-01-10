from swampy.TurtleWorld import *

def square(t,len):
    for i in range(4):
        fd(t,len)
        lt(t)

world = TurtleWorld()
bob = Turtle()
square(bob,150)          # for variable length
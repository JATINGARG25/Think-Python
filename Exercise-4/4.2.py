from swampy.TurtleWorld import *

def polygon(t,len,n):
    angle = 360/n
    for i in range(n):
        fd(t,len)
        lt(t,angle)

world = TurtleWorld()
bob = Turtle()
polygon(bob,75,10)
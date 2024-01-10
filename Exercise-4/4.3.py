from swampy.TurtleWorld import *
import math

def polygon(t,len,n):
    angle = 360/n
    for i in range(n):
        fd(t,len)
        lt(t,angle)

def circle(t,r):
    circumference = 2 * math.pi * r
    n = int(circumference/3) + 1
    len = circumference/n
    polygon(t,len,n)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

circle(bob,100)
wait_for_user()
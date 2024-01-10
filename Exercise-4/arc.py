from swampy.TurtleWorld import *
import math

def polyline(t,len,n,angle):
    for i in range(n):
        fd(t,len)
        lt(t,angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t,step_length,n,step_angle)

def circle(t,r):
    arc(t,r,360)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

circle(bob,35)

wait_for_user()
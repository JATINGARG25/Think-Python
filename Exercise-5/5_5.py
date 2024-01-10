from swampy.TurtleWorld import *

def koch(t, length):

    if length<3:
        fd(t, length)
        return
    m = length/3.0
    koch(t, m)
    lt(t, 60)
    koch(t, m)
    rt(t, 120)
    koch(t, m)
    lt(t, 60)
    koch(t, m)


def snowflake(t, n):

    for i in range(3):
        koch(t, n)
        rt(t, 120)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

snowflake(bob,100)

wait_for_user()

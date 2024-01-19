from swampy.Gui import *

def make_circle():
    canvas.circle([0,0],100,fill="orange",outline="blue",width=5)

j = Gui()
j.title("Welcome To J Interface")
canvas = j.ca(width=250 , height=250 , bg="green")
# canvas.config(bg="green")                       
# item.config(fill="orange",outline="blue",width=10)
button = j.bu(text="Clik Here, For Circle..", command=make_circle)

j.mainloop()
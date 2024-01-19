from swampy.Gui import *

circle = None

def make_circle():
    global circle
    circle = canvas.circle([0,0],100,fill="orange",outline="blue",width=5)

def change_colour():
    if circle == None:
        return
    color = entry.get()
    try:
        circle.config(fill=color)
    except:
        print("You enter wrong color")

j = Gui()
j.title("Welcome To J Interface")
canvas = j.ca(width=250 , height=250 , bg="green")
button = j.bu(text="First Button", command=make_circle)
entry = j.en()
second_button = j.bu(text="Second Button",command=change_colour)
j.mainloop()
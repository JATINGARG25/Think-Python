from swampy.Gui import *

def set_color(color):
    mb.config(text=color)
    # print(color)

g = Gui()
g.title("Interface")
g.la("Select a Color:")
colors = ["red","green","blue","yellow"]
mb = g.mb(text=colors[0])
for color in colors:
    g.mi(mb, text=color, command=Callable(set_color, color))
g.mainloop()

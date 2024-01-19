from swampy.Gui import *

def make_label():
    g.la(text="Thank You.")

g = Gui()                                   # frame
g.title("JATIN")

button = g.bu(text="Press Me")              # for making a button
label = g.la(text="Press the button")       # for labeling (labeled widget)

button2 = g.bu(text="No,Press Me" , command= make_label)
g.mainloop()
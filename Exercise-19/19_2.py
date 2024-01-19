from swampy.Gui import *

def make_label():
    j.la(text="Nice Job!")

def make_button():
    j.bu(text = "Stage 2" , command=make_label)

j = Gui()
j.title("Welcome To J Interface")
button = j.bu(text="Stage 1" , command=make_button)

j.mainloop()
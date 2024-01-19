from swampy.Gui import *

j = Gui()
j.title("Welcome To J Interface")
canvas = j.ca(width=500 , height=500)
canvas.config(bg="green")                       #config is used for doing changing in the canvas -- such as background color,etc..
item = canvas.circle([0,0],100,fill="white")
item.config(fill="orange",outline="blue",width=10) # for changes we use config
j.mainloop()
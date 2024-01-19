from swampy.Gui import *

j = Gui()
j.title("Welcome To J Interface")
canvas = j.ca(width=500 , height=500 , bg="green")
# item = canvas.rectangle([[0, 0], [200, 100]], fill='blue', outline='orange', width=10)
# canvas.oval([[0, 0], [200, 100]], outline='orange', width=10)
# canvas.line([[0, 100], [100, 200], [200, 100]], width=10)
canvas.polygon([[0, 100], [100, 200], [200, 100]],fill="orange",outline="green",width=10)

j.mainloop()
from swampy.World import World

world = World()

canvas = world.ca(width=500, height=500, background='white')

# for making a rectangle
# bbox = [[-150,-100], [150, 100]]
# canvas.rectangle(bbox, outline='black', width=2, fill='green4')

# for making a circle
canvas.circle([-25,0], 70, outline='green',width=2, fill='red')

world.mainloop()
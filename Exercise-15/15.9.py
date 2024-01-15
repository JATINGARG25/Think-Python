from swampy.World import World

world = World()

# National Flag of Czech Republic

canvas = world.ca(width=500, height=500, background='white')
bbox = [[-150,-100], [150, 0]]
bbox2 = [[-150,0], [150,100]]
canvas.rectangle(bbox, fill='red')
canvas.rectangle(bbox2, fill='white')
points = [[-150,-100], [-150, 100], [0, 0]]
canvas.polygon(points, fill='blue4')

world.mainloop()
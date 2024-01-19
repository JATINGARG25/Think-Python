from swampy.TurtleWorld import *
from swampy.World import Interpreter

class SimpleTurtleWorld(TurtleWorld):
        
    def setup(self):

        self.row()
        self.canvas = self.ca(width=400, height=400, bg='white')
        self.col()

        self.gr(cols=2)
        self.bu(text='Print canvas', command=self.canvas.dump)
        self.bu(text='Quit', command=self.quit)
        self.bu(text='Make Turtle', command=self.make_turtle)
        self.bu(text='Clear', command=self.clear)
        self.endgr()

        self.row([0,1], pady=30)
        self.bu(text='Run file', command=self.run_file)
        self.en_file = self.en(text='snowflake.py', width=5)
        self.endrow()

        self.te_code = self.te(width=25, height=10)
        self.te_code.insert(END, 'world.clear()\n')
        self.te_code.insert(END, 'bob = Turtle(world)\n')

        self.bu(text='Run code', command=self.run_text)

if __name__ == '__main__':
    world = SimpleTurtleWorld()
    world.inter = Interpreter(world, globals())
    world.mainloop()
from swampy.Gui import *

j = Gui()
j.title("Welcome To J Interface")
# entry = j.en(text="Default text..")  # for single line
# entry.get()

text = j.te(width=100,height=5)        # for multiple lines
# text.insert(END, 'A line of text.') 
text.insert(2.1,"nothing")
j.mainloop()
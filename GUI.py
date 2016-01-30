from Tkinter import *

master = Tk()

'''
my_entry=Entry(master)
my_entry.pack()
'''

#drop down for choosing level
level = Label(text="Choose a level: ")
level.pack()

var = StringVar(master)
var.set("easy") # initial value

option = OptionMenu(master, var, "easy", "medium", "difficult")
option.pack()


#drop down for choosing register
register = Label(text="Choose a register: ")
register.pack()

var2 = StringVar(master)
var2.set("newspaper") # initial value

option2 = OptionMenu(master, var2, "newspaper", "report", "essay")
option2.pack()

f = Frame(master,height=40, width=300)  #only use integers here


f.pack_propagate(0)
f.pack()

master.title("Complexity analysis")
mainloop()

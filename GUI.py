from Tkinter import *

master = Tk()

'''
my_entry=Entry(master)
my_entry.pack()
'''

def handle_selection():
    print "You've selected >>" + var.get() + "<< as your level. "

def handle_selection2():
    print "You've selected: >>" + var2.get() + "<< as your register. "


#drop down for choosing level
level = Label(text="Choose a level: ")
level.pack()

var = StringVar(master)
var.set("easy") # initial value

option = OptionMenu(master, var, "easy", "medium", "difficult")
option.pack()

selectedLevel = var.get()

#button to display level currently selected
b = Button(master, text="Print selected level?", command=handle_selection)
b.pack()


#drop down for choosing register
register = Label(text="Choose a register: ")
register.pack()

var2 = StringVar(master)
var2.set("newspaper") # initial value

option2 = OptionMenu(master, var2, "newspaper", "report", "essay")
option2.pack()

selectedRegister = var2.get()


#button to display register currently selected
b2 = Button(master, text="Print selected register?", command=handle_selection2)
b2.pack()


f = Frame(master,height=40, width=300)  #only integers to use here
f.pack_propagate(0)
f.pack()

master.title("Complexity analysis")
mainloop()

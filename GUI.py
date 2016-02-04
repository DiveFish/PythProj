from Tkinter import *

master = Tk()


def display_selection_level():
    print "You've selected >>" + level.get() + "<< as your level. "


def display_selection_register():
    print "You've selected: >>" + register.get() + "<< as your register. "

def display_entered_sentence():
    print "You've requested the complexity level of the sentence >>" + userSentence.get() + "<<. "


emptyLine = Label(text=" ")
emptyLine.pack()

# drop down for choosing level
chooseLevel = Label(text="Choose a level: ")
chooseLevel.pack()

level = StringVar(master)
level.set("easy") # initial value

levelOptions = OptionMenu(master, level, "easy", "medium", "difficult")
levelOptions.pack()

selectedLevel = level.get()

# button to display level currently selected
selLev = Button(master, text="Print selected level?", command=display_selection_level)
selLev.pack()

emptyLine = Label(text=" ")
emptyLine.pack()


# drop-down menu for choosing register
chooseRegister = Label(text="Choose a register: ")
chooseRegister.pack()

register = StringVar(master)
register.set("newspaper") # initial value

registerOptions = OptionMenu(master, register, "newspaper", "report", "essay")
registerOptions.pack()

selectedRegister = register.get()


# button to display register currently selected
selReg = Button(master, text="Print selected register?", command=display_selection_register)
selReg.pack()

emptyLine = Label(text=" ")
emptyLine.pack()


# field to enter text for which user wants complexity level
enterSentence = Label(text="Want a sentence of your own evaluated? Just enter it here: ")
enterSentence.pack()
userSentence=Entry(master)
userSentence.pack()

enteredSentence = userSentence.get()

# button to display level currently selected
foreignSent = Button(master, text="Print sentence entered by the user!", command=display_entered_sentence)
foreignSent.pack()


f = Frame(master,height=40, width=300)  # only integers to use here

f.pack_propagate(0)
f.pack()

master.title("Complexity Analysis")
mainloop()

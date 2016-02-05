from Tkinter import *

master = Tk()


def submitted_values():
    print "You've selected the level: " + level.get()
    print "You've selected the register: " + register.get()
    if not userText.get():
        print "No text was entered."
        if not fileName.get():
            print "No filename was entered."
        else:
            print "Warning: the file <" + fileName.get() + "> will be empty."
    else:
        print "You've requested the complexity level of the text: " + userText.get()
        print "It will be saved in the file " + fileName.get()

def save_to_file():
    open(fileName.get() + ".txt", "w").write(userText.get())



emptyLine = Label(text=" ")
emptyLine.pack()


# drop down for choosing level
chooseLevel = Label(text="Choose a level: ")
chooseLevel.pack()

level = StringVar(master)
level.set("easy") # initial value

levelOptions = OptionMenu(master, level, "easy", "advanced", "difficult")
levelOptions.pack()

emptyLine = Label(text=" ")
emptyLine.pack()


# drop-down menu for choosing register
chooseRegister = Label(text="Choose a register: ")
chooseRegister.pack()

register = StringVar(master)
register.set("web chat") # initial value

registerOptions = OptionMenu(master, register, "web chat", "newspaper", "report", "essay")
registerOptions.pack()

emptyLine = Label(text=" ")
emptyLine.pack()


# field to enter text for which user wants complexity level
enterSentence = Label(text="Want a text of your own evaluated? Just enter it here: ")
enterSentence.pack()
userText=Entry(master)
userText.pack()
enterFileName = Label(text="Please name the output file: ")
enterFileName.pack()
fileName=Entry(master)
fileName.pack()


emptyLine = Label(text=" ")
emptyLine.pack()


# button to display level currently selected
unknownText = Button(master, text="Print submitted values!", command=submitted_values)
unknownText.pack()

emptyLine = Label(text=" ")
emptyLine.pack()


# button to display level currently selected
saveToFile = Button(master, text="Save output to a file!", command=save_to_file)
saveToFile.pack()


f = Frame(master,height=40, width=300)  # use only integers here
f.pack_propagate(0)
f.pack()

master.title("Complexity Analysis")
mainloop()

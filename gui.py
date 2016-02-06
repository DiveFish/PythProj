
'''
Created in Jan 2016
@author: Pat
'''


from Tkinter import *

master = Tk()


def submitted_values():
    print "You've selected the level: " + level.get()
    print "You've selected the register: " + register.get()
    if not userText.get():
        print "No text was entered."
        if not fileName.get():
            print "No file name was entered."
        else:
            print "Warning: the file <" + fileName.get() + "> will be empty."
    else:
        print "You've requested the complexity level of the text: " + userText.get()
        print "It will be saved in this file: " + fileName.get()


# can be adapted to actually saving output and not input when the respective methods are ready
def save_to_file():
    wr = open(fileName.get() + ".txt", "w")
    nl = "\n"
    wr.write("You've selected the level: " + level.get() + nl)
    wr.write("You've selected the register: " + register.get() + nl)
    if not userText.get():
        wr.write("No text was entered."  + nl)
        if not fileName.get():
            wr.write("No file name was entered." + nl)
        else:
            wr.write("Warning: the file <" + fileName.get() + "> will be empty." + nl)
    else:
        wr.write("You've requested the complexity level of the text: " + userText.get() + nl)
        wr.write("It was saved in the file called: " + fileName.get() + ".txt" + nl)


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
# field to enter filename where output will be saved
enterFileName = Label(text="Please name the output file: ")
enterFileName.pack()
fileName=Entry(master)
fileName.pack()


emptyLine = Label(text=" ")
emptyLine.pack()


# button to display level currently selected
unknownText = Button(master, text="Print submitted values to screen!", command=submitted_values)
unknownText.pack()

emptyLine = Label(text="OR")
emptyLine.pack()


# button to display level currently selected
saveToFile = Button(master, text="Save all input data to a file!", command=save_to_file)
saveToFile.pack()


f = Frame(master,height=40, width=300)  # use only integers here
f.pack_propagate(0)
f.pack()

master.title("Complexity Analysis")
mainloop()

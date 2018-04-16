from tkinter import *

def doNothing():
    print("This does nothing")
def noRedo():
    print("This cant redo")
def noExit():
    print("You cant exit")


root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="subMenu1", command=doNothing)
subMenu.add_command(label="subMenu2", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=noExit)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="redo", command=noRedo)

# ****** creating toolbar ******

toolbar = Frame(root, bg="blue")

insert = Button(toolbar, text="Button1", command = doNothing)
insert.pack(side=LEFT, padx=2, pady=2)
printbutton = Button(toolbar, text="Button2", command=doNothing)
printbutton.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

root.mainloop

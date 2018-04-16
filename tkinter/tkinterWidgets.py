from tkinter import *

root = Tk()

one = Label(root, text="one", bg="red", fg="white")
one.pack()
two = Label(root, text="two", bg="black", fg="pink")
two.pack(fill=X)
three = Label(root, text="three", bg="green", fg="black")
three.pack(side=LEFT, fill=Y)

root.mainloop()

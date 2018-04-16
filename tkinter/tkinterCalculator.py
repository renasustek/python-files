from tkinter import *

def addition(num1, num2):
     return num1+num2
def subtraction(num1, num2):
     return num1-num2
def multiplication(num1, num2):
     return num1*num2
def division(num1, num2):
     return num1/num2

def clearDisplay():
     display.delete(0,END)
     
def displayValue(text):
     clearDisplay()
     display.insert(0,text)
     
def appendToDisplay(text):
     displayValue(display.get() + text)

def calculate():
     displayedValue = display.get()
     operands = displayedValue.split('+')
     displayValue(addition(int(operands[0]), int(operands[1])))

root = Tk()

display = Entry(root)
display.grid(row=0, column=1, columnspan=4, padx=4, pady=4)

button1 = Button(command=lambda:appendToDisplay("1"),text="1",height = 2, width = 4)
button1.grid(row=1, column=1, padx=2, pady=2)

button2 = Button(command=lambda:appendToDisplay("2"),text="2",height = 2, width = 4)
button2.grid(row=1, column=2, padx=2, pady=2)

button3 = Button(command=lambda:appendToDisplay("3"),text="3",height = 2, width = 4)
button3.grid(row=1, column=3, padx=2, pady=2)

button4 = Button(command=lambda:appendToDisplay("4"),text="4",height = 2, width = 4)
button4.grid(row=2, column=1, padx=2, pady=2)

button5 = Button(command=lambda:appendToDisplay("5"),text="5",height = 2, width = 4)
button5.grid(row=2, column=2, padx=2, pady=2)

button6 = Button(command=lambda:appendToDisplay("6"),text="6",height = 2, width = 4)
button6.grid(row=2, column=3, padx=2, pady=2)

button7 = Button(command=lambda:appendToDisplay("7"),text="7",height = 2, width = 4)
button7.grid(row=3, column=1, padx=2, pady=2)

button8 = Button(command=lambda:appendToDisplay("8"),text="8",height = 2, width = 4)
button8.grid(row=3, column=2, padx=2, pady=2)

button9 = Button(command=lambda:appendToDisplay("9"),text="9",height = 2, width = 4)
button9.grid(row=3, column=3, padx=2, pady=2)

button0 = Button(command=lambda:appendToDisplay("0"),text="0",height = 2, width = 4)
button0.grid(row=4, column=2, padx=2, pady=2)

buttonC = Button(command=lambda:clearDisplay(),text="C",height = 2, width = 4)
buttonC.grid(row=4, column=1, padx=2, pady=2)

buttonE = Button(command=lambda:calculate(),text="=",height = 2, width = 4)
buttonE.grid(row=4, column=3, padx=2, pady=2)

buttonP = Button(command=lambda:appendToDisplay("+"),text="+",height = 2, width = 4)
buttonP.grid(row=1, column=4, padx=2, pady=2)

buttonS = Button(command=lambda:appendToDisplay("-"),text="-",height = 2, width = 4)
buttonS.grid(row=2, column=4, padx=2, pady=2)

buttonM = Button(command=lambda:appendToDisplay("*"),text="*",height = 2, width = 4)
buttonM.grid(row=3, column=4, padx=2, pady=2)

buttonD = Button(command=lambda:appendToDisplay("/"),text="/",height = 2, width = 4)
buttonD.grid(row=4, column=4, padx=2, pady=2)

root.mainloop()


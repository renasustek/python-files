equalsState=False

def addition(num1, num2):
     return num1+num2
def subtraction(num1, num2):
     return num1-num2
def multiplication(num1, num2):
     return num1*num2
def division(num1, num2):
     return num1/num2

def equalsPressed(state):
    global equalsState
    equalsState = state

def clearDisplay():
     display.delete(0,END)
     
def displayValue(text):
     clearDisplay()
     display.insert(0,text)
     
def appendToDisplay(text):
    global equalsState
    if equalsState:
       clearDisplay()
       equalsPressed(False)
    displayValue(display.get() + text)
 

def calculate(): 
     displayedValue = display.get()
     if "+" in displayedValue:
         operands = displayedValue.split('+')
         displayValue(addition(int(operands[0]), int(operands[1])))
     elif "-" in displayedValue:
         operands = displayedValue.split('-')
         displayValue(subtraction(int(operands[0]), int(operands[1])))
     elif "*" in displayedValue:
         operands = displayedValue.split('*')
         displayValue(multiplication(int(operands[0]), int(operands[1])))
     elif "/" in displayedValue:
         operands = displayedValue.split('/')
         displayValue(division(int(operands[0]), int(operands[1])))
     equalsPressed(True)

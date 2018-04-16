def instructions():
     return int(input("Press 1 for addition.\n"+
                    "Press 2 for subtraction\n"+
                    "Press 3 for multiplication\n"+
                    "Press 4 for division\n"+
                    "Press 5 for floor division\n"+
                    "Press 6 for modulo\n"+
                    "Press 7 to find the volume of a cube or cubeoid\n"+
                    "Press 8 to find the circumference of a circle\n"+
                    "press 9 to find the area of a circle\n"+
                    "Press 10 to find the average of 5 No.\n"+
                    "Press 11 to find the average of 4 No.\n"+
                    "Press 12 to find the average of 3 No.\n"+
                    "Press 13 to find the power of somthing\n"+
                    "Press 14 to find the squared root of somthing\n"+
                    ">>>"))

#Addition, Sutraction, Multiplication, Division, Floor Division, Modulo:if choice == 1:

def addition():
     num1 = int(input("Enter first number\n>>> "))
     num2 = int(input("Enter second number\n>>> "))
     answer=num1+num2
     print(num1, "+" , num2 , "=" , answer)
def subtraction():
     num1 = int(input("Enter first number\n>>> "))
     num2 = int(input("Enter second number\n>>> "))
     answer=num1-num2
     print(num1, "-" , num2 , "=" , answer)
def multiplication():
     num1 = int(input("Enter first number\n>>> "))
     num2 = int(input("Enter second number\n>>> "))
     answer=num1*num2
     print(num1, "x" , num2 , "=" , answer)
def division():
     num1 = int(input("Enter first number\n>>> "))
     num2 = int(input("Enter second number\n>>> "))
     answer=num1/num2
     print(num1, "/" , num2 , "=" , answer)
def floor_division():
     num1 = int(input("Enter first number\n>>> "))
     num2 = int(input("Enter second number\n>>> "))
     answer=num1//num2
     print(num1, "//" , num2 , "=" , answer)
def modulo():
     num1 = int(input("Enter first number\n>>> "))
     num2 = int(input("Enter second number\n>>> "))
     answer=num1%num2
     print(num1, "%" , num2 , "=" , answer)

#Volume of a cube or cuboid:

def cube():
     num3 = int(input("enter your 1st number\n>>> "))
     num4 = int(input("enter your 2nd number\n>>> "))
     num5 = int(input("enter your 3rd number\n>>> "))
     unit=input("Enter your unit\n>>> ")
     print("This is the volume of your cube or cuboid", num3 * num4 * num5,unit,"^3")

#To find the area or circumference of a circle:


def circumference():
     unit=input("Enter your unit\n>>> ")
     pi = 3.14159265
     print("This is your cicumference\n>>>",pi ** r,unit,"^2")
def area_circle():
     unit=input("Enter your unit\n>>> ")
     r = int(input("Enter your radius\n>>> "))
     pi = 3.14159265
     print("This is your area\n>>>",2 * pi * r,unit,"^3")

#To find the average of 5,4 and 3 numbers:


def average5():
     num6=int(input("Enter your 1st number\n>>> "))
     num7=int(input("Enter your 2nd number\n>>> "))
     num8=int(input("Enter your 3rd number\n>>> "))
     num9=int(input("Enter your 4th number\n>>> "))
     num10=int(input("Enter your 5th number\n>>> "))
     print("This is your average", num6 + num7 + num8 + num9 + num10 / 5)
def average4():
     num6=int(input("Enter your 1st number\n>>> "))
     num7=int(input("Enter your 2nd number\n>>> "))
     num8=int(input("Enter your 3rd number\n>>> "))
     num9=int(input("Enter your 4th number\n>>> "))
    
     print("This is your average", num6 + num7 + num8 + num9 / 4)
def average3():
     num6=int(input("Enter your 1st number\n>>> "))
     num7=int(input("Enter your 2nd number\n>>> "))
     num8=int(input("Enter your 3rd number\n>>> "))
     print("This is your average", num6 + num7 + num8 / 3)

#Find power and square roots of number:


def power_number():
     num11 = int(input("Enter a number to find the power of\n>>> "))
     power=int(input("Enter a power\n>>> "))
     power_no= num11**power
     print(num11 , "^" , power , "=" , power_no )
def square_root():
    num11=int(input("Enter a number to find the square root\n>>> "))
    print("This is sqared root",num11 ** (1/2))

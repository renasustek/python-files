#Calc is a module contraining all the functions, calc is inside the folder lib.

from lib import calc

response = "y"
    
while response == "y":
     choice = calc.instructions();

#Addition, Sutraction, Multiplication, Division, Floor Division, Modulo:

     if choice == 1:
         calc.addition();
     elif choice == 2:
          calc.subtraction();
     elif choice == 3:
         calc.multiplication();
     elif choice == 4:
          calc.divison();
     elif choice == 5:
         calc.floor_division();
     elif choice == 6:
         calc.modulo();
         
#Volume of a cube or cuboid:

     elif choice == 7:
         calc.cube();

#To find the area or circumference of a circle:

     elif choice == 8:
        calc.circumference ();
     elif choice == 9:
        calc.area_circle ();

#To find the average of 5,4 and 3 numbers:

     elif choice == 10:
         calc.average5();
     elif choice == 11:
         calc.average4();
     elif choice == 12:
         calc.average3();

#Find power and square roots of number:

     elif choice == 13:
         calc.power_number();
     elif choice == 14:
         calc.square_root

#While loop, if user entered y its starts again, if the user enters somthing else it does nothing and the program ends.

     else:
         print("You entered somthing invalid.")

     response=input("Do you want to carry on, press y for yes and n for no:\n")
     if response=="y":
          print("Its going carry on")
     elif response=="n":
          print("ok bye bye now.")
     else:
          print("you need to type y or n")



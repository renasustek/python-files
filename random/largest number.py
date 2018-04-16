print("enter a set of number")
num1=int(input("enter your first choice: "))
num2=int(input("enter your second choice: "))
num3=int(input("enter your third choice: "))
num4=int(input("enter your fourth choice: "))
maxNo = 0
if num1 > maxNo:
    maxNo = num1

if num2 > maxNo:
    maxNo = num2

if num3 > maxNo:
    maxNo = num3
    
if num4 > maxNo:
    maxNo = num4

print(maxNo,", is your greatest number.")
print("ok bye now")
    

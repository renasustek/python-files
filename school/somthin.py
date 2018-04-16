fileExtention = input("What is your file name\n>>")
result=fileExtention.split(".")
if len(result) > 1:
    print("Extention is ."+result[1])
else:
    print("Enter an extention.")



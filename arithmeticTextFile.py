file = open("arithmetic.txt", "w")

whichOperation = input("Which Operation do you want: ")

number1 = input("Enter number 1: ")
number2 = input("Enter number 2: ")
file.write(number1 + whichOperation + number2)

file.close()

file = open("arithmetic.txt", "r")
line = file.readline()
answer = None

file.close()

if whichOperation in line and whichOperation=="+":
    data = line.split(whichOperation)
    answer = int(data[0]) + int(data[1])
elif whichOperation in line and whichOperation=="-":
    data = line.split(whichOperation)
    answer = int(data[0]) - int(data[1])
elif whichOperation in line and whichOperation=="*":
    data = line.split(whichOperation)
    answer = int(data[0]) * int(data[1])
elif whichOperation in line and whichOperation=="/":
    data = line.split(whichOperation)
    answer = int(data[0]) / int(data[1])


else:
    print("This operation is not understood")
    exit(1)
print(line, "=", answer)

# file = open("arithmetic.txt", "w")
#
# number1 = input("Enter number 1: ")
# number2 = input("Enter number 2: ")
# file.write(number1 + "+" + number2)
#
# file.close()

file = open("arithmetic.txt", "r")
line = file.readline()
answer = None

file.close()

if "+" in line:
    data = line.split("+")
    answer = int(data[0]) + int(data[1])
else:
    print("Error: This operation is not understood")
    exit(1)
print(line, "=", answer)

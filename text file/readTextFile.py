file = open("theFile.txt", "r")
line = file.readline()
file.close()
data=line.split("+")
total=int(data[0])+int(data[1])
print(total)

             

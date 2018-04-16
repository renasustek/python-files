reverseSTR= ""

test=input("Enter a word: ")
length=len(test)

for x in range(length-1,-1,-1):
    print(x)
    reverseSTR+=(test[x])
print(reverseSTR)

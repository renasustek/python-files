def convertInchToCm():
    inch = int(input("Enter inches\n>>>"))
    cm = Inch * 2.54
    return cm, "cm"

value, unit = convertInchToCm()
print("conversion",value, unit)

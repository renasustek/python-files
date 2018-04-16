import datetime
person = input('Enter your name: ')
print('Hello', person)
now = datetime.datetime.now()
age = int(input('enter your age: '))
yearsto100 = 100 - age
print("this is when you will be 100: ",yearsto100+now.year)

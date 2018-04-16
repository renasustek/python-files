import random

number=random.randint(1,10)

name=input("please enter your name: ")

print("hello "+name+" how are you today")
print("im thinking of a number between 1 and 10, guess it")

guess=int(input("enter your geuss: "))

while guess!=number:
    if guess < number:
        print("your guess is too low, guess again")
        guess=int(input("enter your geuss:"))
    else:
        print("your guess is too high, guess again")
        guess=int(input("enter your geuss:"))


print("well done you win")

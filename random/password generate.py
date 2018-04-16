import random
answer="y"
while answer =="y":
    pw_length = int(input("how long do you want your password from 4 to 20\nEnter your choice: "))
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if pw_length <=3:
        print("your password is to short")
    elif pw_length >=21:
        print("your password is to long")
    else:
        mypw = ""
        for x in range(pw_length):
            next_index = random.randrange(len(alphabet))
            mypw = mypw + alphabet[next_index]
        print(mypw)
        answer=input("do you want to generate a password press y to get another password and n to quit>>>:")
        if answer=="n":
            print("ok bye")
        else:
            print("press either y or n.")                        

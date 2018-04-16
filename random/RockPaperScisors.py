import random
counter=0
turns=0
comp=""



while turns <6:
    turns +=1
    print(turns)
    ranNum=random.randint(0,2)
    if ranNum==0:
        comp="rock"
    if ranNum==1:
        comp="paper"
    if ranNum==2:
        comp="scissors"

    human=input("Enter your choice, out of rock, paper, scissors:\n")
    
    if human==comp:
        print("Its a draw.")
    elif human=="rock" and comp=="scissors":
        print("you, WIN!")
        counter+=1
    elif human=="paper" and comp=="rock":
        print("you, WIN!")
        counter+=1
    elif human=="paper" and comp=="scissors":
        print("you, WIN!")
        counter+=1
    elif human=="scissors" and comp=="paper":
        print("you WIN!")
        counter+=1
    elif human=="rock" and comp=="paper":
        print("you, lose.")
        counter-=1
    elif human=="scissors" and comp=="rock":
        print("you lose.")
        counter-=1    
    else:
        print("You entered somthing wrong, try again.")
        turns-=1
    
    print("Your points:",counter)
    if turns==5:
            if counter==2:
                    print("You got bronze.")
            elif counter==3:
                    print("you got silver.")
            elif counter==4:
                    print("you got gold.")
            elif counter==5:
                    print ("you got diamond.")
            else:
                    print("you are horrible at this!.")

            yn=input("Do you want to carry on, press y for yes and n for no:\n")
            if yn=="y":
                    counter=0
                    turns==0
                    print("Its going carry on")
            elif yn=="n":
                    print("ok bye bye now.")
            else:
                    print("you need to type y or n")
                    

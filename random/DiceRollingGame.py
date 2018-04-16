import random

AmountOfTimePlayed=0
playerOneCounter=0
playerTwoCounter=0

player1=input("What is the name of player one\n>>>")
player2=input("What is the name of player two\n>>>")

while AmountOfTimePlayed == 0:
    AmountOfTimePlayed+=1
    
    PlayerOneNumber=random.randint(1,6)
    print("The number",player1,"rolled was",PlayerOneNumber)
    PlayerTwoNumber=random.randint(1,6)
    print("The number",player2,"rolled was",PlayerTwoNumber)
    
    if PlayerOneNumber<PlayerTwoNumber:
        print(player2,"Loses this round.")
        playerTwoCounter+=1
    elif PlayerOneNumber==PlayerTwoNumber:
        print("Its a draw.")
    else:
        print(player1,"wins this round.")
        playerOneCounter+=1

    print(player1,"score is",playerOneCounter)
    print(player2,"Your score is",playerTwoCounter)

    carryOn=input("Would you like to carry on, y for yes and n for no\n>>>")
    if carryOn == "y" or carryOn == "yes":
        print()
        AmountOfTimePlayed=0
    elif carryOn == "n" or carryOn == "no":
        if PlayerOneNumber<PlayerTwoNumber:
            if player2 == "ali":
                print(player2,"You win the game.")
                o
            else:
                print(player2,"You win the game.")
        elif PlayerOneNumber>PlayerTwoNumber:
            if player2=="ali" or player1=="ali":
                print(player1,"You win the game.")
                print("im allowed to play playsation after the holiday hahai dont care if u didnt agree")
            else:
                print(player1,"You win the game.")
        else:
            print("Its a draw")
            

        
    else:
        print("You didn't input what I asked so bye.")


           

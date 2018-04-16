totalGoals=0
games=int(input("How many matches were there?\n>>>"))
for x in range(games):
    goals=int(input("Enter the amuont of goals scored\n>>>"))
    totalGoals=totalGoals+goals
print("there were this many goals",str(totalGoals))
average=totalGoals/games
print("this is your average goals",str(average))



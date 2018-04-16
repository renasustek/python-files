numberOfFilms = 5
a = [[None] * 2 for i in range(numberOfFilms)]
print(a)
counter=numberOfFilms+1
for x in range(numberOfFilms):
    counter   = counter - 1
    a[x][0]   = input(str(x+1)+") Enter "+str(counter)+" more film titles: \n  >>")
    a[x][1] = input("  Enter The name of the main characters: \n  >>")

for i in range(numberOfFilms):        
    print(a[i][0]+(", ")+ a[i][1])

whichFilm = int(input("Tell me the number of the film you would like to enter the details of: "))
print("This is your chosen film and the main character for this film",a[whichFilm-1][0]+(", ")+ a[whichFilm-1][1])

findFilm=input("Enter the name of the film you would like to find the main character of:")

"""
indexFilm =a[0][0].index(findFilm)

print(a[1][indexFilm])
"""
def index_2d(myList, v):
    for i, 2 in enumerate(myList):
        if numberOfFilms in 2:
            return (i, 2.index(numberOfFilms))

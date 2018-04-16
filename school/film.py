numberOfFilms = 2

film =[None] * numberOfFilms
mainCa=[None] * numberOfFilms
counter=numberOfFilms+1
for x in range(numberOfFilms):
    counter   = counter - 1
    film[x]   = input(str(x+1)+") Enter "+str(counter)+" more film titles: \n  >>")
    mainCa[x] = input("  Enter The name of the main characters: \n  >>")

for i in range(numberOfFilms):        
    print(film[i]+(", ")+ mainCa[i])

whichFilm = int(input("Tell me the number of the film you would like to enter the details of: "))
print("This is your chosen film and the main character for this film",film[whichFilm-1]+(", ")+ mainCa[whichFilm-1])

findFilm=input("Enter the name of the film you would like to find the main character of:")

indexFilm = film.index(findFilm)

print(mainCa[indexFilm])

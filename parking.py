import os
os.system("cls")

PARKING_PLACES = 7
FREE_PLACE = 3

print("#"*PARKING_PLACES*5)

for place_index in range(1, PARKING_PLACES + 1):
    if place_index== FREE_PLACE:
        print("|   |",end="")
    else:
        print("| X |", end="")


print("\n","#"*PARKING_PLACES*5, sep="")
#"sep=" - este separator 
# datorita caruia semnul "#" este afisat pe ecran unul dupa alul
# in caz contrar se va afisha " " in locuri nepotrivite

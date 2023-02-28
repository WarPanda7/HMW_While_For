import os
os.system('cls')
#small_ship = int(input("Introduceti coordonata vaporului"))
# big_ship = "wWw"
big_ship = int(input("Introduceti coordonata vaporului"))
for x in range(1,11):
    if x== big_ship-1:
       print( "w", end="" )
    elif x== big_ship+1:
       print( "w", end="" )   
    elif x == big_ship:
      print( "W", end="" )
    else:
      print( "~", end="" )

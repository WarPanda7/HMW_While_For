import os
from msvcrt import getch
import random
######## DATA ########
gmap=[["  ","  ","  ","  ","  "],
      ["  ","  ","  ","  ","  "],
      ["  ","  ","  ","  ","  "],
      ["  ","  ","  ","  ","  "],
      ["  ","  ","  ","  ","  "]]
mouse="🐁"
cat="🐱"
robo_r=random.randint(0,4)
robo_c=random.randint(0,4)
gmap[robo_r][robo_c]=cat

mouse_r=random.randint(0,4)
mouse_c=random.randint(0,4)
gmap[mouse_c][mouse_r]=mouse

free="  "
cat_hit=100
mouse_hp=100
while gmap[mouse_c][mouse_r]==gmap[robo_r][robo_c]:
    robo_r=random.randint(0,4)
    robo_c=random.randint(0,4)
    mouse_r=random.randint(0,4)
    mouse_c=random.randint(0,4)

while True:
    os.system("cls")

   
    ######## MAP ########
    print("-"*17)
    for r in range(5):
        print("|",end="")
        for c in range(5):
            print(gmap[r][c], end=" ")
        print("|")
    print("-"*17)
    print("*Mouse HP:",mouse_hp,"*")
    print("Controls:\na-left\nd-right\nw-up\ns-down\nx-exit")

    if mouse_hp<=0:
         print("\n!!!CAT WIN!!!")
         break
    ########## MOVE #############
    option = getch()
    if option ==b"a":
            if robo_c in range(1,5):
                gmap[robo_r][robo_c] = free
                robo_c-=1
                gmap[robo_r][robo_c] = cat
            else:
                gmap[robo_r][robo_c] = free
                gmap[robo_r][robo_c] = cat
    elif option ==b"d":
            if robo_c in range(0,4):
                gmap[robo_r][robo_c] = free
                robo_c+=1
                gmap[robo_r][robo_c] = cat
            else:
                gmap[robo_r][robo_c] = free
                gmap[robo_r][robo_c] = cat
    elif option ==b"s":
            if robo_r in range(0,4):
                gmap[robo_r][robo_c] = free
                robo_r+=1
                gmap[robo_r][robo_c] = cat
            else:
                gmap[robo_r][robo_c] = free
                gmap[robo_r][robo_c] = cat
    elif option ==b"w":
            if robo_r in range(1,5):
                gmap[robo_r][robo_c] = free
                robo_r-=1
                gmap[robo_r][robo_c] = cat
            else:
                gmap[robo_r][robo_c] = free
                gmap[robo_r][robo_c] = cat
    elif option==b"x":
        print("Game over")
        break

    ######### END GAME #########
    if gmap[mouse_c][mouse_r]==gmap[robo_r][robo_c]:
        mouse_hp=mouse_hp-cat_hit
   
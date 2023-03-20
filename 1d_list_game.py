import os
from msvcrt import getch
import random
# Data #
gmap=[" "," "," "," "," "," "," "," "," "," "]
robo_x=random.randint(0,len(gmap)-1)
gmap[robo_x]="X"
random_enemy=random.randint(0, len(gmap)-1)
robot_hp=100
bomb_hit=30
# Start Game #
while True:
    os.system("cls")
    if random_enemy !=robo_x:
        gmap[random_enemy]="B"
    else:
        random_enemy=random.randint(0, len(gmap)-1)
    # MAP #
    print("#"*41)
    print("| ",end="")
    for i in range(len(gmap)):
        print(gmap[i], end=" | ")
    print()
    print("#"*41)
    print("| ",end="")
    for i in range(len(gmap)):
        print(i, end=" | ")
    print("\n\n"," "*13,"*Robot HP:",robot_hp,"*",sep="")
    print("\n Controls:\n a-left, d-right, x-exit") 
    #Controls#
    option = getch() #
    zero=0
    last=len(gmap)-1
    if robo_x in range(1,len(gmap)-1):
        if option ==b"a":
            gmap[robo_x] = " " #remove from the current position
            robo_x-=1
            gmap[robo_x]= "X"
        elif option ==b"d":
            gmap[robo_x] = " " #remove from the current position
            robo_x+=1
            gmap[robo_x]= "X"
    elif robo_x==zero:
        if option ==b"d":
            gmap[robo_x] = " " #remove from the current position
            robo_x+=1
            gmap[robo_x]= "X"
    elif robo_x==last: 
         if option ==b"a":
            gmap[robo_x] = " " #remove from the current position
            robo_x-=1
            gmap[robo_x]= "X"
    if option==b"x":
            print("Game Over")
            break
    if robo_x==random_enemy:
        robot_hp=robot_hp-bomb_hit
        while random_enemy==robo_x:
            random_enemy=random.randint(0, len(gmap)-1)
    if robot_hp<=0:
        print("\n\n GAVE OVER, ROBOT IS DEAD!!!")
        break       
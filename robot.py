import os
os.system("cls")

robot_lvl = int(5)
box_type= "ߛ"
box_count= int(3)
robot_with_box = True
robot_direction = "up"

#robot_direction = 'up'
for i in range(1,15):
    if i==robot_lvl-1 and robot_direction== "up":
        print("ߡ")
    elif i==robot_lvl:
        if robot_with_box== True:
            print('𐠲',box_type*box_count)
        else: 
            print('𐠲')
    elif i==robot_lvl+1 and robot_direction=="down":
        print("ߜ")
    else : 
        print("..")

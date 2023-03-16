import os
os.system("cls")
p =["Mercedes",None,"BMW",None,None,"Toyota","BMW","Audi"]
p_f=[]
user_car_brand=input("Name of your Car")
user_park_index=int(input("What place?"))
# If Parking place is closeed, print free spaces.
while user_car_brand not in p:
    if p[user_park_index]==None:
        print("Ok, park there!")
        p[user_park_index]=user_car_brand
        break
    else:
        print("Parking lot is occupied")
        for f in range(len(p)):
            if p[f]==None:
                if f not in p_f:
                    p_f.append(f)
        print("Free Parking lots:",p_f)
        user_park_index=int(input("What place do you choice for park?"))
#Print Statistic of car brands.
p_unic_mark=set(p)
p_unic_mark.remove(None)
for s in p_unic_mark:
    car_m = p.count(s)
    print(s,":",car_m)
# List of parking Cars with park time.
hours =[  1.20,0   ,2.30 ,0   ,0   ,3       ,4.35 ,9.10]
for h in range(len(p)):
    if p[h]!=None:
        print("Parking lot:",h,"Model:",p[h],"Time:",hours[h],"hours")
#Statistics (free/total) places in parking
total= len(p)
free= 0
for i in range(len(p)):
    if p[i]==None:
        free+=1
print("Parking (Free/Total)",free,"/",total,"places")

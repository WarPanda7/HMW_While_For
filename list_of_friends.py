import os
os.system("cls")
name=[]
while len(name) < 100:
    friends=input("what is your fiends Name?")
    if friends=="":
        break
    if friends not in name:
        name.append(friends)
    else:
        print("Acest prieten a fost deja introdus.")
for i in range(len(name)):
    print("    ",i ,">>>" ,name[i])

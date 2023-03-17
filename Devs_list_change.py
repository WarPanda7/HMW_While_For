import os
os.system("cls")

people=["Johny","Andrew","Marry","Sam","Tomy"]
print("BEFORE", people)

placeA=int(input("Change who?(0,1,2,3,4)"))
while True:
    if placeA<0 or placeA>len(people)-1:
        print("Error,Try again:")
        placeA=int(input("Change who?(0,1,2,3,4)"))
    else:
        break
placeB=int(input("With Who?(0,1,2,3,4)"))
while True:
    if placeB<0 or placeB>len(people)-1:
        print("Error,Try again:")
        placeB=int(input("With Who?(0,1,2,3,4)"))
    else:
        break
print(len(people))
temp=people[placeB]
people[placeB]=people[placeA]
people[placeA]=temp

print("AFTER", people)

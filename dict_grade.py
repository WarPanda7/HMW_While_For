student1={"Firstname":"Andrew", "Lastname":"Woods", "age":23, "grade_1":8, "grade_2":9,"grade_3":8}
x=student1.get("grade_1")
y=student1.get("grade_2")
z=student1.get("grade_3")
media=(x+y+z)/3 

for i, k in student1.items():
    if i=="grade_1" or i=="grade_2" or i=="grade_3":
        print(i,'{:.2f}'.format(student1[i])) 
    else:
        print(i,k)
print("Media este:",'{:.2f}'.format(media))
if media>=5:
    print("Felicitari:",student1.get("Firstname"),student1.get("Lastname"),"A trecut Examenul")
else:
    print("Studentul:",student1.get("Firstname"),student1.get("Lastname"),"Nu a trecut examenul")

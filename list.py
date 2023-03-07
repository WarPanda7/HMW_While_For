import os
os.system("cls")
marks = [[
    [8,5,6,9,7 ],
    [6,8,9,5,6 ],
    [5,7,8,7,9 ]
    ],[
    [9,9,6,9,7 ],
    [7,5,8,5,6 ],
    [9,8,9,9,9 ]
    ]]
for gi in range(2):
    print("Group ",gi+1,":\n","---------------------------",sep="")
    print("Lesson| 1 | 2 | 3 | 4 | 5 |")
    for si in range(3):
        print("St:",si+1,end=" | ",)
        
        for li in range(5):
            print(marks[gi][si][li],end=" | ")
        print()
    print("---------------------------")
print()
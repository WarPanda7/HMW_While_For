import os
os.system("cls")

grades={"English":8,"Math":7, "Anatomy":9, "Biology":8, "Algebre":6, "History":7}
for key, value in grades.items():
    print(value, key)

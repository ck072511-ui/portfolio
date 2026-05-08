# grade student based on mark mark >=90,grade = "a",90>mark>80,grade = "b",80>mark>70,grade = "c",70>mark,grade  "d"
marks = int(input("enter marks :="))

if (marks>= 90):
    grade = "A"
elif(marks>= 80 and marks< 90):
    grade = "B"
elif (marks>= 70 and marks< 80):
    garde = "C"
else:
    grade = "D"

print("stedent grade :=",grade)
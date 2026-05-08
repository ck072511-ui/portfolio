#Write a Python script to find the average of 5 subjects and calculate the grade (A/B/C).
a = 96
b = 89
c = 87
d = 78
e = 82
avg = (a+b+c+d+e)/5
if avg >= 80:
    grade = "A"
elif avg >= 75:
    grade = "B"
else:
    grade = "C"
print("average:",avg,"grade:",grade)



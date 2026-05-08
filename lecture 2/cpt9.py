# grade calculator: problem - assign a latter grade based on a students score :
# A(90-100),B(80-89),C(70-79),D(60-69),F(bellow 60):

score = int(input("student score for exam :="))

if (score >= 90 and score < 100):
    grade = "A"
elif (score >= 80 and score < 89):
    grade = "B"
elif (score >= 70 and score < 79):
    grade = "C"
elif (score >= 60 and score < 69):
    grade = "D"
else:
    grade = "F"

print("student score for grade :=",grade)
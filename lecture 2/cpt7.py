# age group categorization,classify a person age group; Child <13,teenager(13-19),adult(20-29)senior(60+);

age = int(input("enter your age :="))

if (age < 13):
    print("Child")
elif (age > 13 and age < 19):
    print("Teenager")
elif (age > 20 and age < 29):
    print("Adult")
elif (age > 30 and age < 60):
    print("Senior")
else:
    print("Old Senior")
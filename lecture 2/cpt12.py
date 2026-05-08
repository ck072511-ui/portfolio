# leap year checker :
# problem :- determine if a year is a leap year (leap year are divisble by 4 , but not by 100 unless also divisible by 400):

year = int(input("enter year :="))

if (year % 4 == 0):
    print("its a leap year :=",year)
else:
    print("its a not leap year :=",year)
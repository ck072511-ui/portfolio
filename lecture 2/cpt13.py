# Write a program to check whether a number is a multiple of 3 or 7.

num = int(input("enter number :="))

if (num % 3 == 0 or num % 7 == 0):
    print("number is multiple of 3 or 7 :=",num)
else:
    print("number is not multiple of 3 or 7")

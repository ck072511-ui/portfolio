# wap to find the greatest number entered by the user 

num1 = int(input("enter first number :="))
num2 = int(input("enter second number :="))
num3 = int(input("enter third number :="))
if (num1 >= num2 and num1 >= num3):
    print("largest first number :=",num1)
elif (num2 >= num3):
    print("largest second number :=",num2)
else:
    print("largest third number :=",num3)
# password strength checker : 
# problem : check if a password is weak, medium, strong
# criteria < 6 char(weak),6-10 char (medium),>10 char (strong)

password = input("enter your paasword :=")

if (len(password) < 6):
    password = 'weak'
elif (len(password) > 6 and len(password) < 10):
    password = 'medium'
else:
    password = 'stronge'

print("password set in char accodding :=",password)
# movie ticket pricing:-  movie ticket price on based on age $ 12 for adults (18 and over),
# $8 for children everyone gets a $2 discount on wednesday:

age = int(input("enter your age :="))
day ='wednesday'
price = 12
if age >= 18:
    price = 12
else:
    price = 8
if (day =='wednesday'):
    price = price - 2

print("movie ticket on price based :=",price)


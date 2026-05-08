# Take user input for principal, rate, and time — compute compound interest.
p = int(input("enter principal value:="))
r = int(input("enter rate value:="))
t = int(input("enter time value:="))
ci = p*((1+r/100)**t)-p
print("compound_interest:",ci)
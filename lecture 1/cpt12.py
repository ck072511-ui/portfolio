# Write a program to find the area of a triangle using Heron’s formula.
import math
a = float(input("Side a: "))
b = float(input("Side b: "))
c = float(input("Side c: "))
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("Area:", area)


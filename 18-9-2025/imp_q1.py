"""
swap 2 numbers with using 3rd variable
"""

num1 = 10
num2 = 20
num3 = 0

num3 = num1
num1 = num2
num2 = num3

print(f"num 1 = {num1} , num 2 = {num2}")

# swap 2 numbers without using 3rd variable

a = 10
b = 20
print(f"A = {a} , B = {b} ")
a,b = b,a # just python can do that not any ather programing legvage do 
print(f"A = {a} , B = {b} ")

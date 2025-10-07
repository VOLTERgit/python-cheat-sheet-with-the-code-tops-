"""
accept 2 number from user and perform addition operation

type(): which type of value store in a variable.
type casting : to convert one data type value into another data type.
    syntax : datatype(value)
        
        = int ("10")

        = float ("10")

        =str(10) // "10"
"""

num1 = input("enter your 1st number: ")
num2 = input("enter your 2nd number: ")

ans = num1 + num2

print(f"your sub {ans} ")

print(type(num1))

num3 = int(input("enter number 1: "))

num4 = int(input("enter number 2: "))

ans1 = num3 + num4 

print(f"{num3} + {num4} = {ans1}")

print(type(num3))

"""
Nested if statement : when condition inside the another condition

syntax :
if condition:
    if condition:
        statement
    else:
        statement
    else:
    if condition:
        statement
    else:
        statement
"""

marks = int(input("Enter marks"))

if marks >= 0 and marks <=100:
    if marks >=70:
        print("A grade")
    elif marks >=60 and marks <70:
        print("B grade")
    elif marks >= 50 and marks <70:
        print("C grade")
    elif marks >=40 and marks <70:
        print("D grade")
    else:
        print("Fail")
else:
    print("Invalid mark !!!")
"""
elif statement ::: when there are multiple conditions 

syntax : 

if condition :
    statement
elif condition :
    statement
elif condition :
    statement
else:
    statement
"""
mark = int(input("Enter your marks :"))
if mark >=70:
    print("A grade")
elif mark >=60 and mark <70:
    print("B grade")
elif mark >= 50 and mark <70:
    print("C grade")
elif mark >=40 and mark <70:
    print("D grade")
else:
    print("Fail")

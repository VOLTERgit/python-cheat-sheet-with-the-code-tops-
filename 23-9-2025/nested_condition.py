num1 = int(input("Enter the number 1 : "))
num2 = int(input("Enter the number 2 : "))
num3 = int(input("Enter the number 3 : "))

if num1 > num2:
    if num1 > num3:
        print("Number 1 is greater")
    else:
        print("Number 3 is greater")
else:
    if num2 > num3:
        print("Number 2 is greater")
    else:
        print("number 3 is greater")

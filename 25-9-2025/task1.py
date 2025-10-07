"""Accept 5 number from user and calculate total positive numbers and total negative numbers

Output :::
Enter a number : 5
Enter a number : - 4
Enter a number : 6
Enter a number : -2
Enter a number : 5 

total positive nos are : 3
total negative nos are : 2

"""

ans = 0
num2 = 0 # positive
num3 = 0 # negative
for i in range(5):
    num = int(input("Enter a number : "))
    if num > 0:
        num2 += 1
    else:
        num3 += 1
print(f"Total positive nos are : {num2}") # positive output
print(f"Total negative nos are : {num3}") # negative output
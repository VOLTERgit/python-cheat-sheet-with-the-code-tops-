"""
Accept 5 numbers from user and calculate total even nos are there and total 
    odd numbers are there
"""
# num = 0
even = 0
odd = 0
for i in range(1,6):
    num = int(input("Enter the  : "))
    if num %2 == 0:
        even += 1
    else:
        odd += 1
print(f"Your total even number {even} ")
print(f"Your total odd number {odd}")
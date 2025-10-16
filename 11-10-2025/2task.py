"""
accept 5 numbers from user and store even numbers in even list and odd nubers in odd list.
"""

odd = []
eve = []
for i in range(1,5):
    num1 = int(input("Enter the number :"))
    if num1 %2 != 0:
        odd.append(num1)
    elif num1 %2 == 0:
        eve.append(num1)
print(f"even list = {eve}")

print(f"odd list = {odd}")
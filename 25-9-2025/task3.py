"""
accept 5 number from users and calculate even nos sum and odd nos sum
"""
even_sum = 0
odd_sum = 0

for i in range(1,6):
    num = int(input("Enter the number : "))
    if num %2 == 0:
        even_sum += num
    else:
        odd_sum += num

print(f"your sum of even {even_sum}")
print(f"your sum of odd {odd_sum}")

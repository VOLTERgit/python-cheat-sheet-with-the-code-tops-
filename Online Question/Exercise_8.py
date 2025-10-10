"""
Exercise 8: Print the following pattern

1
22
333
4444
55555
"""
num = int(input("Enter the number: "))

for i in range(num+1):
    for j in range(i):
        print(f"{i}", end=" ")
    print()


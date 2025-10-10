# Merge two lists using the following condition
"""
Given two lists of numbers, write Python code to create a new list containing odd numbers from the first list and even numbers from the second list.
"""

num1 = [10,20,25,30,35] # odd numbers
num2 = [40,45,60,75,90] # even numbers
num3 = []

# for i in range(len(num1)-1):
j = len(num1)
numa = 0
for i in range(j):
    if num1[i] %2 != 0: 
        num3.append(num1[i])
for i in range(j):
    if num2[i] %2 == 0:
        num3.append(num2[i])

print (num3)

"""
Display numbers divisible by 5
Write a Python code to display numbers from a list divisible by 5
"""

num1 = [10,20,33,46,55]
tops = 0
# arr = len(num1)-1
# print(arr)
while tops <= len(num1)-1:
    if num1[tops]%5 == 0:
        print(num1[tops])
    tops +=1
    
    # print()
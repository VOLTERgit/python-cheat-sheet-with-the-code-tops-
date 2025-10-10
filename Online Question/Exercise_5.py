"""
Check if the first and last numbers of a list are the same 

Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.
"""
num1 = [11,22,33,44,55,11]
num2 = [21,22,23,24,25,26]
if num1[0] == num1[len(num1)-1]:
    print("1st array - True")
else:
    print("F1st array - False")

if num2[0] == num2[len(num1)-1]:
    print(" 2st array - True")
else:
    print("2st array - False")
    



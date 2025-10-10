"""
Exercise 9: Check Palindrome Number
Write a Python code to check if the given number is a palindrome. A palindrome number reads the same forwards and backward. For example, 545 is a palindrome number.
"""
palindrom = int(input("Enter the number: "))

re_palindrom = str(palindrom)
re_palindrom1 = re_palindrom[::-1] 
if str(palindrom) == re_palindrom1:
    print("Yes it's a palindrom number ")
else:
    print("No it's not palindrom number")


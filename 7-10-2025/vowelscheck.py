"""
check string contain vowels or not

"""

s1 = "python"

status = False
no_of_vowels = 0

for char in s1:
    if char in "aeiou":
        no_of_vowels +=1
        status = True
print(status)
print("No of vowels = ", no_of_vowels)

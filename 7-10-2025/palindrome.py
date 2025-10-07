# reverse string 

s1 = "python"

print(s1[:]) # python
print(s1[::]) # python
print(s1[::-1]) #nohtyp

#to check string is palindrome or not 
# e.g. wow mom

reverse = s1[::-1]

if reverse == s1:
    print("Yes its palindrome")
else:
    print("No, its not a palindrome")

s2 = "WOW"

reverse_s2 = s2 [::-1]

if reverse_s2 == s2:
    print("Yes its palindrome")
else:
    print("No, its not a palindrome")
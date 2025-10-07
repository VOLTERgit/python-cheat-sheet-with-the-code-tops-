"""
0  1  2  3   (positive indexing)
j  a  v  a
-4 -3 -2- 1  (negative indexing)
"""
# string slicing 
s1 = "java"
#fetch last character from the string
print(s1[-1])

# string slicing - fetch first 2 characters from the string
print(s1[0:2]) # JA

#or
#ja
print(s1[:2]) # by default it will start from 0

# fetch next 2 characters from middle

print(s1[1:3]) # AV

#string using of negative indexing::
print(s1[-3:-1]) #AV

#java : fetch only AVA
print(s1[-3:]) # by default it will end with -1

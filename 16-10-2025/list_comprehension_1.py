"""
store 1 to 5 numbers in list
"""

# without list comprehension

l1 = []

for i in range(1,6):
    l1.append(i)

print(l1)
print("----------------------")

# with list comprehension 
#    2         1
#  value      loop

l1 = [i for i in range(1,6)]
print(l1)

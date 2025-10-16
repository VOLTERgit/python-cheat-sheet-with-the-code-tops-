"""
pop(): it will remove specific index wise
"""

fruit_list = ["Apple","Banana","Mango", "Grapes", "Kiwi"]

print(fruit_list)

print(len(fruit_list))

index_value = int(input("Enter index position which value you want to remove : "))

if index_value >= 0 and index_value < len(fruit_list):
    fruit_list.pop(index_value)
    print(fruit_list)
else:
    print("Index position does not exist !!! ")

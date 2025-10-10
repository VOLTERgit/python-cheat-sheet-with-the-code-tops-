
num1 = [10,20,25,30,35] # odd numbers
num2 = [40,45,60,75,90] # even numbers
num3 = []

# for i in range(len(num1)-1):
j = len(num1)

for i in range(j):
    if num1[i] %2 != 0:
        num3[i] = num1[i]
        i+=1
    elif num2[i] %2 == 0:
        num3[i] = num2[i]
print (num3)
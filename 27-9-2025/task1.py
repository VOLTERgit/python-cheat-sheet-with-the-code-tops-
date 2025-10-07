status = True
sum = 0 
while status:
    num1 = int(input("Enter a Number : "))
    sum += num1
    
    choice = input("if you want to closs the program add n , if not press y : ")
    if choice == 'n' or choice == 'no':
        status = False
    elif choice == 'y' or choice == 'yes':
        status = True
    else:
        print("Invalid input")

print(f"your sum is sum = {sum}")

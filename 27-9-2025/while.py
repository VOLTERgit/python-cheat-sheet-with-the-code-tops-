"""
initlization
while condition:
    statement
    updation
"""

status = True # initlization
while status:
    num = int (input("Enter a nnumber : "))

    choice = input("Do you want to add more number press 'y' for yes and press 'n' for no : ")
    if choice == 'y' or choice == 'yes':
        status = True
    else:
        status = False


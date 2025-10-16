product_list = [] #blank list
menu = """
        menu

    1) press 1 for add record
    2) press 2 for remove record
    3) press 3 for view record

"""

status = True
while status:
    print(menu)
    choice = int(input("Enter your choice : "))
    if choice == 1:

        product = input("Enter your product :: ")
        if product in product_list:
            print("Product is all redy add ")
        else:
            product_list.append(product)
            print("Product Added Successfully !!")

    elif choice == 2:
        product = input("Enter Which product you want to remove ? ")
        if product in product_list:
            product_list.remove(product)
            print("Product removed successfully !!! ")
        else:
            print("Product does not exists !!! ")
        
    elif choice == 3:
        print("Records :::::: ")
        for record in product_list:
            print(record)
    else:
        print("Invalid choice ")

    menu_choice = input("Do you want to perform more operations press 'y' for yes and press 'n' for no: ").lower()

    if menu_choice == 'n' or menu_choice == 'no':
        status = False
    else:
        status = True
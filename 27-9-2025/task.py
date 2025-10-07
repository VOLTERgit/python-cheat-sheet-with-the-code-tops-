"""
accept only even nos.
"""
status = True
while status:
    num = int(input("Enter the nubmer even number only : "))
    if num %2== 0:
        status = True
    else:
        print("No you Enter the odd number ")
        status = False

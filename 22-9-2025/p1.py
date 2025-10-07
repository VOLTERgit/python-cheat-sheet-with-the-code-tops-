# len = i use that function to count the streag in the variable 
name = input("Enter Your Name :")

# count = len(name) # if you want to use new variable

if len(name) < 3:
    print("name must be at least 3 characters")
elif len(name) > 50:
    print("name can be a maxiam of 50 characters")
else:
    print("name look good")


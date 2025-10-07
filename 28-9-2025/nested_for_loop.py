"""
When loop cal inside the another loop its called nested loop

syntax : 
for var in sequence : 
    for var in sequence: 
    statement

"""
for row in range(1,6):
    for col in range(1,6):
        print("*", end = " ")
    print()

"""
looping concept :

    theree are mainly 2 types of looping statement

    1) for loop
    2)while loop

1) for loop : for loop is an sequenced controlled loop.
    which is ececute no. of time.

        syntax :
    
    for var in sequence:
        statements
"""
"""
range ([start], stop, [step]):

syntax :
    range(2,6) # 2 3 4 5

    range(5) # 0 1 2 3 4

    range(1,7,2) # start, stop,step
                # 1 3 5
"""
# for -- itereter 
for i in range(6): # by default start from 0 to 5
    print(i)

for i in range (1,6):
    print(f"({i}) hello")
    
for i in range (1, 6):
    print(i,end=" ")

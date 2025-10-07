"""
A
B C
D E F
G H I J
"""
char = 65
for row in range(1,6):
    for col in range(row+1):
        print(chr(char), end = " ")
        char += 1
    print()
    
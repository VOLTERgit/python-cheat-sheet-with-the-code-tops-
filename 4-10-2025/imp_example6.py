name = "pyThoN"

result = ""

for char in name:
    if char.islower():
        result+=char.upper()
    else:
        result+=char.lower()

print(result)
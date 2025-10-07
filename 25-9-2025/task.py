"""accept 5 number from user and calculate addition"""
ans = 0
for i in range(5):
    num = int(input("Enter a number : "))
    ans += num
print(f"your sum {ans}")
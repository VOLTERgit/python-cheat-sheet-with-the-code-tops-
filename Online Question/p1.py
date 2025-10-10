fr = input("Enter your fruits: ")
total = 0
contiti = int(input("Enter How much you want: "))
# for i in range(contiti):
if fr == "Mango" or fr == "manga":
    total =30*contiti 
elif fr == "Banana":
    total =40*contiti
else:
    print("Sry we do not shlee that product ")
print(f"Your total amount is {total} ")
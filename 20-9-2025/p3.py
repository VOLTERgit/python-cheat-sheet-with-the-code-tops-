
num = int(input('Enter a number that you want to check divisible: '))

if num % 2 == 0:
    if num % 3 == 0:
        print('The number is divisible by 2 and 3.')
    else:
        print('The number is divisible by 2, but not divisible by 3.')
else:
    if num % 3 == 0:
        print('The number is divisible by 3, but not divisible by 2')
    else:
        print('The number is not divisible 2 and 3.')
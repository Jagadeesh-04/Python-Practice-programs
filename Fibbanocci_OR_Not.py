# Check the given number is in the fibbanocci series or not!
n = 10000000000 # Limit of the fibbanocci series
number = int(input('Enter the value you want to check : '))
if n<0:
    print("Enter positive numbers")
else:
    a = 0
    b = 1
    for i in range(2,n):
        c = a + b
        a = b
        b = c
        if b<=number:
            if b == number:
                break
        else:
            break
if b == number:
    print("The given number is in a fibbanocci series ")
else:
    print("The given number is not in a fibbanocci series")
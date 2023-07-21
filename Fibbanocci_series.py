# Finding the values of fibbanocci series upto 'n' number !

while True:
    num = int(input("Enter the limit of fibbanocci series :"))
    if num<0:
        print("Enter positive numbers")
    else:
        #The starting points always fixed one || 0 and 1 ||
        a = 0
        b = 1
        for i in range(2,num):
            c = a+b
            a = b
            b = c
        print(f'The value for fibbanocci series Limit of {num} is : {c}')
        break

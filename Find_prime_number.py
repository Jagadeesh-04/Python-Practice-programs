# Python program to print prime number
# A prime number is a number which is divided by 1 and that number itself .

num = int(input('Enter The Number:'))
for i in range(2,num):
    if num%i==0:
        print('The Given Number is not a Prime Number')
        break
else:
    print('The Given Number is a Prime Number')
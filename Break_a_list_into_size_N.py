#Break a list into chunks of size N in Python

l =[1,2,3,4,5,6,7,8,9]
n = int(input('how many elements your list want to contains ? : '))
print("The list after breaking is :")
for i in range(0,len(l),n):
    print(l[i:i+n] , end = ' ')
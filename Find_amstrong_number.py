# program to find the given number is amstrong or not!

a = input()
b = [int(i) for i in a ]
c=0
for j in b:
    c = c+(j**3)
    
if int(a) == c:
    print('The Given Number is an Amstrong Number')
else:
    print('The Given Number is Not an Amstrong Number')
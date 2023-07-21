# program to find the factorial
# Using while loop
num = int(input('Enter The Number :'))
if num==0 or num==1:
    print('The Factorial of the given numer is : ',int('1'))
else:
    i = 1
    while num>0:
        i=i*num
        num-=1
    
print(f'The Factorial of the given numer is : {i}')

#____________________________________________________________________________

# program to find the factorial
# Using For loop
num = int(input('Enter The Number :'))
if num==0 or num==1:
    print('The Factorial of the given numer is : ',int('1'))
ans = 1
for i in range(1,num+1):
    ans = ans*i
print(f'The Factorial of the given numer is : {ans}')
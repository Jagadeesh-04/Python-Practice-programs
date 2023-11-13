
'''
# Array Programs :
# Create one array
from array import *
 
ar = array('i',[1,23,4,5,6]) # creating array with the elements yo want

print(ar)
'''

# program to find the sum of an array elements
# Get input form the user
def total():
    s = 0
    for i in arr:
        s+=int(i)
    print("Your given array is :",arr)
    return f'The sum of the given array is : {s}'

arr=input('Enter the array values : \nGive all array elements at once ,to show the difference add space between each elements :').split()
print(total())



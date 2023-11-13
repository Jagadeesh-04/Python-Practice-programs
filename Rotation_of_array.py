# Rotation of array 
# Rotate the array with the number you want at first
arr=input('Enter the array values !\nGive all array elements at once ,to show the difference add space between each elements :').split()
array =list(map(lambda x : int(x) ,arr))
print("Your array is :",array)
r=int(input('Enter the rotation point [ Enter the position [1 to n] of the element you want to be first ] :'))
n = len(array)
if r-1>=n:
    print('Array is out of length')
else:
    temp = array[:r-1]
    print("Your array is :",array)
    print("The rotation of your array is :",array[r-1:]+temp)

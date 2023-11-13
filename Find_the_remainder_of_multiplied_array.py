# Python Program to Find remainder of an array multiplication 
# The multiplication of array is divided by number "n"

arr=input('Enter the array values !\nGive all array elements at once ,to show the difference add space between each elements :').split()
array =list(map(lambda x : int(x) ,arr))
print("Your array is :",array)
n = int(input('Enter the value to divid the array : '))
temp = 1
for i in array:
    temp = temp * i
ans =temp//n
print(ans) 



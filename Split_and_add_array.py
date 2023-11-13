# Python program to split array and printing the elements in rotation order
# Get the inputs from the users
def split(array,d):
    t1 = array[d-1:]
    t2 = array[:d-1]
    return t1+t2

# Creating array
arr=input('Enter the array values !\nGive all array elements at once ,to show the difference add space between each elements :').split()
array =list(map(lambda x : int(x) ,arr))
print("Your array is :",array)
d = int(input('Enter the position [1 to n] , to be splited : '))
print(split(array,d))

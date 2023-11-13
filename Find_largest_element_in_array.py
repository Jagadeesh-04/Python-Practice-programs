# program to find the largest element in an array
def large():
    s = 0
    for i in arr:
        if int(i) > int(s):
            s = i
    print("Your array is : ",arr)
    return f'Largest element in the given array is : {s}'

arr=input('Enter the array values !\nGive all array elements at once ,to show the difference add space between each elements :').split()
print(large())

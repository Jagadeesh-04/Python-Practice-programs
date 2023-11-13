# program for given array is monotic or not!
# a monotic series is a series which all elements that presents in the arrray is
# - either in a ascending order or descenting order .
def mon(a):
    b = 0  
    for i in range(len(a)-1):
        if a[i] <= a[i+1]:
            b = b + 1
    if b == len(a)-1 :
        return True

def mon1(a):
    b = 0
    for i in range(len(a)-1):
        if a[i] >= a[i+1]:
            b = b + 1 
    if b == len(a)-1 :
        return True

arr=input('Enter the array values !\nGive all array elements at once ,to show the difference add space between each elements :').split()
a =list(map(lambda x : int(x) ,arr))
print("Your array is :",a)

print('Given array is Monotic'if mon(a) or mon1(a) else 'Given array is not a Monotic')

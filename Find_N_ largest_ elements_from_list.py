#program to find N largest elements from a list

def nlarge(li):
    temp=[]
    for i in range(0,n):
        max = i 
        for j in list1:
            if max < j:
                max = j
        list1.remove(max)
        temp.append(max)
    return temp
list2 =[12,35,75,96,47,85,77,63]
list1 = list2
n = int(input('Enter the limit of large numbers : '))
print(f"The {n} number of largest elements in the list is : {nlarge(list1)}")
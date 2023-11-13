#program to print odd numbers in a list

list1 = [2, 7, 5, 64, 14, 12, 34, 75, 42, 51]
t1 = []
for i,a in enumerate(list1):
    if a%2 !=0:
        t1.append(a)
print("Total Odd numbers in a given list is :",t1)

#program to print even numbers in a list
list2 = [2, 7, 5, 64, 14, 12, 34, 75, 42, 51]
t2 = []
for i,a in enumerate(list1):
    if a%2==0:
        t2.append(a)
print("Total Even numbers in a given list is :",t2)

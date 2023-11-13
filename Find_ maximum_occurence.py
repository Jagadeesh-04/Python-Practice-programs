# program to print the maximum occurences of the element in the list :

string1 = input("Enter the string : ")
l1=[]
for i in string1:
    c=0
    for j in string1:
        if j == i:
            c+=1
    l1.append([i,c])
t1 = 0
t2 = 0
for i in l1:
    if i[1]>t2:
        t1 = i[0]
        t2 = i[1]
print(f"The maximum number of occurance in a given list is [{t1}]\n'{t1}' occurs {t2} times in a given list ") 



#alter_way...

from typing import Counter

string1 = input("Enter the string : ")
b = Counter(string1)
t1 = 0
for i in b.values():
    if i > t1:
        t1 = i
for i,j in b.items():
    if j == t1 :
        print(f"The maximum number of occurance in a given list is : {i}\n'{i}' occurs '{j}' times in a given list ")
        break
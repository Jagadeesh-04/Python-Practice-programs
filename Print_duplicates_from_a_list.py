# Program to print duplicates from a list of integers

list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
l2 =[]
for i in list:
    if list.count(i)>1:
        if i not in l2:
            l2.append(i)
print("Total duplicate elements from a given list is :",l2)
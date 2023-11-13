#program to find Cumulative sum of a list

list1 = [10, 20, 30, 40, 50]
l = []
b = 0
for i in list1:
    b += i
    l.append(b)
print("The cumulative sum of the list is :",l)

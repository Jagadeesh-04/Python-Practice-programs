# program to print negative numbers in a list

list1 = [0, -1, 2, -7, -5, 64, 14]
negative_num =[]
for i in list1:
    if i < 0:
        negative_num.append(i)
print("Total Negative numbers presents in a given list is :",negative_num)

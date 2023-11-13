# Sort the values of first list using second list

list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [ 0, 1, 1, 0, 1, 2, 2, 0, 1]
list3 =[]
# combine both list1 and list2 using zip
combined = zip(list2,list1)
# using sorted function
for i,j in sorted(combined):
    list3.append(j)
print("The list after sorted using 2nd list :",list3)
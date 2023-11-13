# Removing multiple elements from a given list

list1 = [2,4,5,6,7,8,9,1]
rem = [4,2,6] # elements need to remove
new =  [] #new_list
for i in list1:
    if i in rem:
        continue
    else:
        new.append(i)
print("Elements in the list after removal :",new)
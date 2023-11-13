#code to  Remove empty List 
test_list = [5, 6, [], 3, [], [], 9]
b= []
for i in test_list:
    if i:
        b.append(i)
print("The list elements after removing empty list is :",b)
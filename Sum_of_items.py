# program to find the sum of all items in a dictionary

a =  {'a': 100, 'b': 200, 'c': 300}
b = 0
for i in a.values():
    b+=int(i)
print("Total sum of the dictionary value is :",b)
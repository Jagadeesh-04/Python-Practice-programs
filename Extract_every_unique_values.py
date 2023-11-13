# Extract Unique values in dictionary 

d = {'python' : [5, 6, 7, 8],
   'is' : [10, 11, 7, 5],
   'best' : [6, 12, 10, 8],
   'for' : [1, 2, 5]}
a=[]
for i in d.values():
    for j in i:
        if j not in a:
            a.append(j)
a.sort()
print("Values that presents in a dictionary is :",a)
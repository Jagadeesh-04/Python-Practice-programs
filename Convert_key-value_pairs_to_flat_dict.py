#Convert key-values list to flat dictionary

dict1={"name": ['aa','bb','cc','dd'], "age":[1,2,3,4]}
l1=[]
b = zip(dict1['name'],dict1['age'])
for i in b:
    l1.append(i)

print("The dicionary is :",dict(l1))

#program to find which element presents maximum times in the given list
# using collection module

import collections as c

std = [1,6,8,5,5,4,3,2,8,2,6,9,3,5,1]
val_count = c.Counter(std)
higher = 0
value = 0
for i,j in val_count.items():
        if j > higher:
            higher = j
            value = i
print(f'The value with maximum occurance in the given list is : {value}\nWhich occurance in the given list is : {higher} times')



### Collection module deque operation

import collections as c

listof = c.deque([2,3,5,6])
try:
    listof.append('this_one')
except Exception as e:
    print(e)
else:
    print(listof)


# using chainmap

import collections as c
a = {1:3}
b = {2:4}
print(c.ChainMap(a,b))

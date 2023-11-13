# Sum of list element digits in a given List
# Ex : list = [23]   o/p : 2+3 = 5

list1 = [12,34,56,76,43,85,29]
print('The Given list is :',list1)
sums = []
for i in list1:
    a = 0
    for j in str(i):
        a += int(j)
    sums.append(a)
print('Sum of number digits in the given List is :',sums)
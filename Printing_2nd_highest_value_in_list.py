#Printing the 2nd highest value in the given list

a = [12,3,43,56,47,97,22,99,65,68,9,5,22]
b = 0
c = 0
for i in range(len(a)):
    if b < a[i]:
        b = a[i]
for i in range(len(a)):
        if a[i] > c and b > a[i] :
            c = a[i]
print("The 2nd largest element in the given list is :",c)
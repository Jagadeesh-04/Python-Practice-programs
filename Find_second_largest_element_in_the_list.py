# Python program to find second largest element in the list
# approach 1

list1 = [10, 20, 4, 45, 99] #list elements
temp = set(list1)
temp.remove(max(temp))
print("The second largest element in the given list is :",max(temp))


# Approach 2
list2 = [16, 24, 38, 45, 99, 85, 72] #list elements
temp = 0
second = 0
for i in range(len(list2)):
    if list2[i] > temp:
        temp = list2[i]
for i in range(len(list2)):
    if list2[i] > second and list2[i] < temp:
        second = list2[i]

print("The second largest element in the given list is :",second)
#  program to find sum of elements in list

list1 = []
# Creating a list 
tem = int(input("Enter the length of the list :"))
for i in range(1,tem+1):
    num = int(input(f"Enter the {i}.position list element :"))
    list1.append(num)
# adding the list elements
sum = 0
for i in list1:
    sum += i
print("The sum of the given list is :",sum)
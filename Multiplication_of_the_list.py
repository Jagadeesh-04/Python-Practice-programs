#  program to find multiplication of the total elements in the list

list1 = []
# Creating a list 
tem = int(input("Enter the length of the list : "))
for i in range(1,tem+1):
    num = int(input(f"Enter the {i}.position list element : "))
    list1.append(num)
# Multiplying the list elements
mul = 1
for i in list1:
    mul *= i
print("The Multiplication of the given list is :",mul)
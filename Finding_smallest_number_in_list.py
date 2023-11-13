# Program to find the smallest element in a list

# To create a list
'''list1 = []
# Creating a list 
tem = int(input("Enter the length of the list :"))
for i in range(1,tem+1):
    num = int(input(f"Enter the {i}.position list element :"))
    list1.append(num) '''

list1 = [12, 15, 3, 10] # fixed list
smallest = list1[0]
for i in list1:
    if smallest > i:
        smallest = i 
print("The smallest element in the given list is : ",smallest)

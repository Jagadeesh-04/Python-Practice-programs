# Program to reverse a list 
# approach 1  , we can use inbuild methods

list1 = [1,3,5,7,9]  # enter your list
print("Your original list is :",list1)
list1.reverse()
print("The reversed list is :",list1) 

 #or
# we can get that through our own codes !

list1 = [10, 11, 12, 13, 14, 15] # enter your list
print("Your original list is :",list1) 
list2 = []
for i in list1:
    list2.insert(0,i)
print("The reversed list is :",list2) 


## Count the Number of matching characters in a pair of string

a = input("Enter the 1st string :")
b = input("Enter the 2nd string :")
c = 0 
for i in set(a):
    if i in set(b):
        c+=1
print("The matching characters count in a given string is :",c)
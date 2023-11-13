# creating dict based on user input

n = int(input("Enter the no.of total dictionary elements :"))
dict1 = {}
for i in range(n):
    name = input("Enter the Key : ")
    dict1[name] = input("Enter the value : ")
print("Your dictionary is : ",dict1)
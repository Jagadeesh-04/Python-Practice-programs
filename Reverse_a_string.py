# Program to reverse words of string

string = input('Enter the word : ')
l1 = []
for i in string :
    l1.insert(0,i)
print(f"The original string is :{string}\nString after reverse is :{''.join(l1)}")
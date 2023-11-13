# Remove all duplicate values from a given string in Python

text1 = input("Enter the string :")
t2 = ''
for i in text1:
    if i not in t2:
        t2+=i
print(t2)
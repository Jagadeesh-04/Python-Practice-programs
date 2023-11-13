# Program to check if a string contains any special character

string=input("Enter the string :")
b = 0
for i in string:
    if i.isalnum():
        continue
    else:
        b+=1
print("The given string doesn't contains any special characters" if b==0 else "The given string contains special characters !")
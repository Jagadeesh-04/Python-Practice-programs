# Program to remove particular character from string 
# we have other methods but here we use replace method and passing empty character in needed places 
string = input("Enter the string :")
letter = input('Enter the letter you want to remove : ')
for i in range(len(string)-1):
    if string[i] == letter :
        string2 = string.replace(string[i],'')
        break
print(f"Original string is :{string}\nString after removal :{string2}")
# program to demonstrate Maximum Frequent Character in String

string = input("Enter the string :")
print("The original string is : ",string)
string_freq = {}
for i in string:
    if i in string_freq:
        string_freq[i] += 1
    else:
        string_freq[i] = 1
lfc = ''
t = 0
for j,k in string_freq.items():
    if k > t :
        t = k
for key,val in string_freq.items():
    if val == t:
        lfc += key
print("The most appeard character/characters in the given string is :",lfc)

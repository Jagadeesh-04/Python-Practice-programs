# program to demonstrate Least Frequent(appeared) Character in the given String

string = input("Enter the string :")
print("The original string is : ",string)
string_freq = {}
for i in string:
    if i in string_freq:
        string_freq[i] += 1
    else:
        string_freq[i] = 1
lfc = ''
for i in  range(1,len(string_freq)+1): 
    for j,k in string_freq.items():
        if i == k:
            lfc += j
    if lfc:
        break     
print("The least appeard character/characters in the given string is :",lfc)


#program for removing i-th character from a string

string = "Jagadeeshwaran"
rem = 5
for i in range(len(string)):
    if rem == i:
        b=string.replace(string[i],'',1)
print("The original string is :",string)
print("The string after removing i-th element is :",b)
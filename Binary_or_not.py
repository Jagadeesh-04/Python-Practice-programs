
# Check if a given string is binary string or not

string = "0101010101abc0"
b = len(string)
c = 0
for i in string:
    if i.isnumeric():
        if int(i)==0 or int(i)==1:
            c+=1
if c==b:
    print('The given string is binary string')
else:
    print('The given string is not a binary string')

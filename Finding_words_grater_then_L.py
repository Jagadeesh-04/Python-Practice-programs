## Find 'words' which are greater than given length k

string = "The given string doesn't contains any special characters" #input("enter the sentence :")
# Here 'any' is the word only with less than length 4 
l = 4
tem= list(string.split())
c=''
for i in tem:
    if len(i)>l:
        c += i+' '
print(c)

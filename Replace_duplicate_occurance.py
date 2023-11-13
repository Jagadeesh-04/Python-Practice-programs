# Replace duplicate Occurrence in String

string = input("Enter the string :") # Ex: Malayalam
rep = input("Enter the element you want to replace with duplicate_elements :") # Ex: '_'
tem=''
for i in string:
    if i not in tem:
        tem+=i
    else:
        tem+= rep
print("The string after replacing is :",tem)

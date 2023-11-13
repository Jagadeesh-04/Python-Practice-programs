## program to find uncommon words from two Strings

string1 = input("Enter the 1st string :").split()
string2 = input("Enter the 2nd string :").split()
s3 = [i for i in string1 if i not in string2]
s2 = [i for i in string2 if i not in string1]
print("The uncommon words from a given lists is :",s2+s3)
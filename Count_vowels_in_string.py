##Program to accept the strings which contains all vowels

a = input("Enter the string :")
b = a
c = [b.count('a'), b.count('e'),b.count('i'),b.count('o'),b.count('u')]
if 0 in c:
    print('NO ,The given string "Not" contain all the vowels')
else:
    print('YES ,The given string contains all the vowels')
# program to check whether the string is Symmetrical or Palindrome

string = input('Enter the word : ')
a = len(string)//2
if string[:a] == string[a:] or string[:a]==string[a+1:]:
    print('The given string is symetric')
else:
    print('The given string is NOT symetric') 
if string == string[::-1]:
    print(f'The given string {string} is Palindrome')
else:
    print(f'The given string {string} is not a Palindrome')

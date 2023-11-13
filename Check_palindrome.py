#program to check if a string is palindrome or not !

string = input('Enter the word : ')
if string == string[::-1]:
    print(f'The given string {string} is Palindrome')
else:
    print(f'The given string {string} is not a Palindrome')
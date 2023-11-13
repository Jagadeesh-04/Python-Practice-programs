# program to Remove a key from dictionary

dictionary = {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22, 'Mani': 21}
print("The given dictionary is :",dictionary.items())
c = input('Enter a Key name to delete : ')
dictionary.pop(c)
print("The dictionary after removing a key is :",dictionary)

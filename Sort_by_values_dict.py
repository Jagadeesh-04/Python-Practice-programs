# Python program to sort... list of dictionaries by values in Python

list1 = [{"name": "Nandini", "age": 20},
 {"name": "Manjeet", "age": 20},
 {"name": "Nikhil", "age": 19}]

print("The list of dictionary after sorted by age is :",sorted(list1,key=lambda i:(i['age'],i ['name'])))
# Python code to count the number of occurrences

lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = int(input('Enter the element to be searched : '))
count = 0
if x > 0:
    for ele in lst:
        if (ele == x):
            count = count + 1
else:
    print('Enter a valid number')

print(f"The given number is present '{count}' times in a given list")

### or use .count() operation

print(f"The given number is present '{lst.count(x)}' times in a given list")
# Create a list , and get the inputs from the user

# 1st we need the length of the list
n = int(input('Enter the length of the list: '))
values = []
for i in range(1,n+1):
    # Get the inputs from the user
    a = int(input(f'Enter the no.{i} list value: '))
    #append the values in an empty list
    values.append(a)

print(f'your List is : {values}')
# Python program to swap first and last element of a list
# approch 1 ,
# list(element 1),element(-1) = list(element -1),element(1)

### OR
def swap(values):

	temp = values[0]
	values[0] = values[- 1]
	values[- 1] = temp
	return values

n = int(input('Enter the length of the list: '))
values = []
for i in range(1,n+1):
    # Get the inputs from the user
    a = int(input(f'Enter the no.{i} list value: '))
    #append the values in an empty list
    values.append(a)

print(f'your List is : {values}')
print("The list after swapping is :",swap(values))

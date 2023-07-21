# Python program to print all prime number in an interval

x = 2
y = int(input("Enter the number :"))
prime_list = []
for i in range(x, y):
	if i == 0 or i == 1:
		continue
	else:
		for j in range(2, int(i/2+1)):
			if i % j == 0:
				break
		else:
			prime_list.append(i)
print("The list of the prime numbers with in the particular interval is :",prime_list)

    

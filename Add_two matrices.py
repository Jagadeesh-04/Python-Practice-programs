# Program to add two matrices 

M1 = [[1,2,2,3],
	[4,5,6,7],
	[7,8,9,2]]

M2 = [[9,8,5,7],
	[6,5,5,4],
	[3,2,4,1]]


result = [[0,0,0,0],
		[0,0,0,0],
		[0,0,0,0]]

# iterate through rows
for i in range(len(M1)):
# iterate through columns
    for j in range(len(M1[0])):
        result[i][j] +=  M1[i][j] + M2[i][j]
            
print("The addition of Two matrices is : ",result)


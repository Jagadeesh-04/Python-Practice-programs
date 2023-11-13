# Calculate the sum of cubes for n numbers
# calculating cubes for every numbers upto the user given number and results the answer by adding them 

num = int(input('Enter the limit : '))
temp= 1
ans = 0
c = 0
while num >= temp:
    c = temp * temp *temp
    ans += c
    c = 0
    temp +=1

print("The sum of cubes upto the given number is : ",ans)
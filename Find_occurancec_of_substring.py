# find the occurences of sub str  in str:
# finding how many times a substring occurs in original string
string = 'ABCDCDC' #input()
sub_string ='CDC'  #input()
count = 0
while len(string) >= len(sub_string):
    x = string[:len(sub_string)]
    if sub_string == x:
        count +=1
    string = string [1:]  
print("Total number of occurences of substring in the original string is :",count)          

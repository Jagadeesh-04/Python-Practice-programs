# program to change every small letter into a capital letter of each word
sen = 'he is a good boy'
tem = sen.split()
ans=[]
for i in tem:
    ans.append(i.capitalize())
print(' '.join(ans)) 
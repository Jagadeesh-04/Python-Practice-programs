# using exception handling
# just a checking like how to use !

try:
    print('*'/5)
except Exception as e:
    print(type(e),'||',e)
else:
    print('it works')
finally:
    print('loop done')
   

try:
    a = int(input("Enter anything :"))
    if a == 0:
        print('something')
    elif a==1:
        print('its one')
    else:
        print('Give valid input')
except:
    print('Give some valid input')

   
def aaa():
    n = int(input("Enter integers :"))
    return n
try:
    print(aaa())
except Exception as e:
    print(type(e),'\n',e)

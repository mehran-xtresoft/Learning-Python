x=int(input("please enter input:  "))
print(x)
if x<0:
    x=0
    print(x)
    print('negative changed to zero')

elif x==0:
    print('zero')
elif x==1:
    print('one')
else:
    print('greater than one')
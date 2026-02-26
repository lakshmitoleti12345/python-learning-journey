'''num=153
n=str(num)
sum=0
for i in n:
    sum+=int(i)**3
if sum==num:
    print("armstrong")
'''
#user input 

num=int(input("enter a number:"))
n=len(str(num))
sum=0
for i in str(num):
    sum+=int(i)**n
if sum==num:
    print("armastrong")
else:
    print("not armastrong")    
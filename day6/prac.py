 '''n=19
if(n&1)==0:
    print("even")
else:
    print("odd")'''
'''n=0
if n>0:
    print("pos")
elif n==0:
    print("zero")
else:
    print("neg")'''
'''a,b,c=1000,300,500
if (a>b and a>c):
    print("a is greater")
elif (b>a and b>c):
    print("b is greater")
else:
    print("c is greater")'''
# leap year
'''year=int(input("enter a year:"))
if(year%400==0 or(year%4==0 and year%100!=0)):
    print(year,"is a leap year")
else:
    print(year ,"is not leap year")'''
#grade calculator
'''marks=int(input("enter your marks:"))
if marks>=90:
    print("grade A")
elif marks>=80:
    print("grade B")
elif marks<80 and marks>=70:
    print("grade C")
else:
    print("fail")'''
# 1 to 100 numbers
'''n=100
for i in range(1,n+1):
    print(i,end=" ")'''
## even nubers between 1 to 50
'''n=50
for i in range(1,n+1):
    if(i%2==0):
        print(i,end=" ")'''
# sum of n natural numbers
'''n=10
sum=0
for i in range(n):
    sum +=i
print(sum)'''
#factorial of a number 5! =5*4*3*2*1=
'''n=3
fac=1
for i in range(n,0,-1):
   fac=fac*i
print(fac)'''
# reverse a number by using loop
'''n=12345
rev=" "
while n>0:
    rev=rev+str(n%10)
    n=n//10
print(rev)'''
#right angle triangle pattern
'''n=5
for i in range(5):
    for j in range(1+i):
        print("*",end=" ")
    print(end="\n")'''
#inverted traingle
'''n=5
for i in range(5):
    for j in range(5-i):
        print("*",end=" ")
    print()'''
# pyramid
'''for i in range(10):
    for k in range(10-i):
        print(end=" " )
    for j in range(i):
        print("*",end=" ")
    print()'''
# reverse pyramid
'''for i in range(10):
    for k in range(i):
        print(end=" ")
    for j in range(10-i):
        print("*", end= " ")
    print()'''
#number triangle
'''for i in range(5):
    for k in range(5-i):
        print(end=" " )
    for j in range(i):
        print(i,end=" ")
    print()'''
#check palindrome string
'''name="abbab"
n=len(name)
print(n)
rev=""
for i in range(n,0,-1):
    print(name[i-1])
    rev=rev+name[i-1]
print(rev)
if rev==name:
    print("palindrome")
else:
    print("not palindrome")'''
#vowels and consonat count
'''s="satyalakshmi"
n=len(s)
count=0
for i in s:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        count +=1
print(count,"is count of vowels")
'''
#reverse a string without slicing
'''s="abb123"
n=len(s)
rev=""
for i in range(n-1,-1,-1):
    rev=rev+s[i]
print(rev)'''
#remove duplicates from strig
'''s="aabbcdettyy"
new=""
for i in s:
    if i not in new:
        new=new+i
print(new)
print(s)'''
'''s="masaladosa"
new=""
for i in s:
    if i not in new:
        count=0
        for j in s:
            if i==j:
               count +=1
        print(i,count)
        new +=i
        '''
'''for i in range(5, 5):
    print(i)
for i in range(2):
    print("hello")
else:
    print("else block")'''
#print even and odd numbers from given number in 

'''while n>0:
    rem=n%10
    if rem%2==0:
        print(rem,"is even")
    else:
        print(rem,"is odd")
    n=n//10'''
n=12345
sum=0
count=0
rem=0
while n>0:
    rem=rem*10+n%10
    sum=sum+rem
    count=count+1
    n=n//10
print(sum)
print(count)
 


  




        
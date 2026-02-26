n=int(input("enter a number"))
reverse=0
while n>0:
    digit=n%10
    reverse*=10+digit
    n//=10
if(n==reverse):
        print("palindrome")
else:
        print("not palindrome")

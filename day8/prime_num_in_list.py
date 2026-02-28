n=[2,4,5,7,8,12,11,17,26,23,51]
'''for i in n:
    if i>1:
        is_prime=True
        for j in range(2,i):
            if i%j==0:
                is_prime=False
                break
        if is_prime:
            print(i,"is prime")'''
for i in n:
    if i>1:
        is_prime=True
        for j in range(2,i):
           if(i%j==0):
               is_prime=False
               break
        if is_prime:
            print(i)
    




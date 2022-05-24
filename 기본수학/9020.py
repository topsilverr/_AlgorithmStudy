def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True

t=int(input())

for i in range(t):
    n=int(input())
    a,b=n//2,n//2

    while a>0:
        if isPrime(a) and isPrime(b):
            print(a,b)
            break
        else:
            a-=1
            b+=1

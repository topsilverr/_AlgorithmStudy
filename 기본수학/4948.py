def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True

list=list(range(2,246912))
sosu=[]
for i in list:
    if isPrime(i):
        sosu.append(i)


while True:
    count=0
    n=int(input())
    if n==0:
        break
    else:
        for i in sosu:
            if n<i<=2*n:
                count+=1
        print(count)
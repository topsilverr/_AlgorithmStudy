def isPrime(num):
    if num == 1:
        return False
    else:
        for n in range(2, int(num ** 0.5) + 1):
            if num % n == 0:
                return False
        return True

n, m = map(int, input().split())

for i in range(n,m+1):
    if isPrime(i):
        print(i)

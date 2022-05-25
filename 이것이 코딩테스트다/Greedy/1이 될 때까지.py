n,k=map(int,input().split())
res=0

while True:
    if n==1: # 이미 1이면 res는 0
        break
    elif n%k==0: # n이 k의 배수면
        while True: # n이 1이 될 때까지 계속 나눠줌
            if n==1:
                break
            else:
                n = n // k
                res += 1
    else: # 그것도 아니면
        while True: # n이 k의 배수가 될 때까지 1빼주기
            if n%k==0:
                break
            else:
                n = n - 1
                res += 1


print(res)
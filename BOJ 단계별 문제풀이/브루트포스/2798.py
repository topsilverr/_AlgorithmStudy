n,m=map(int,input().split())
num=list(map(int,input().split()))

num.sort(reverse=True)

for a in num:
    if a >= m:
        del a # 굳이

for a in num:



n,m=map(int,input().split())
num=list(map(int,input().split()))

num.sort(reverse=True)
result = 0

for a in num:
    if a >= m:
        del a # 굳이

for i in range(0,len(num)):
    for j in range(i+1,len(num)):
        for k in range(i+2,len(num)):
            if num[i]+num[j]+num[k] > m :
                continue
            else:
                result=max(result,num[i]+num[j]+num[k])

print(result)
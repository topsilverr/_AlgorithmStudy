n,m,k=map(int,input().split())
arr=list(map(int,input().split())) # 배열로 받기,,,,

arr.sort()
res=0
if arr[n-1]==arr[n-2]:
    res=arr[0]*m
else:
    while True:
        for i in range(k):
            if m == 0:
                break
            res+=arr[n-1]
            m-=1
        if m==0:
            break
        res+=arr[n-2]
        m-=1

print(res)
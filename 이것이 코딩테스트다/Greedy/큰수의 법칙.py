n,m,k=map(int,input().split())
arr=list(map(int,input().split())) # 배열로 받기,,,,

arr.sort()
res=0
if arr[n-1]==arr[n-2]: # 큰 수 두개가 같은 경우
    res=arr[0]*m
else:
    while True:
        for i in range(k): # 한 세트 만들기
            if m == 0:
                break
            res+=arr[n-1] # 가장 큰 수 K번 더하기
            m-=1
        if m==0:
            break
        res+=arr[n-2] # 중간중간 가림막 만들기 => 두번째로 큰 수로 가림막 만들기
        m-=1

print(res)
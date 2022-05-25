n,m=map(int,input().split())
res=[] # 가장 작은 수를 저장할 배열
for i in range(n):
    arr=[]
    arr=list(map(int,input().split()))
    arr.sort() # 가장 작은 수를 배열의 처음으로 보내기 위해
    res.append(arr[0]) #가장 작은 수를 res 배열에 저장

print(max(res)) # 가장 작은 수들 중 가장 큰 수를 출력
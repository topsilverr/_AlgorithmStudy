n,k=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(int(input()))
res=0
arr.sort(reverse=True) # 내림차순으로 정렬 -> arr=arr.sort() 는 불가 할당하려면 arr=sorted(arr) 로 사용
for i in range(n):
    if k//arr[i]>=1: # k를 동전으로 나눈 값이 1 이상이면 k 속에 동전이 포함된다는 뜻
        res+=k//arr[i] # 몫만큼 동전 사용 가능
        k=k-(arr[i]*(k//arr[i])) # k 값 조정

print(res)
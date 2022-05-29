n=int(input())
arr=[]

# 그리디 문제 => 정렬은 필수 라고 생각하기 ~
# 제일 먼저 시작하고 & 제일 먼저 끝나는 회의 를 먼저 진행해야 더 많은 회의 진행 가능 !

for i in range(n): # 아래처럼 저장하는 방법 기억하기!
    start,end=map(int,input().split())
    arr.append([start,end]) # 이중 배열로 저장

arr=sorted(arr,key=lambda a:a[0]) # 시작 시간 기준으로 먼저 정렬 후
arr=sorted(arr,key=lambda a:a[1]) # 종료 시간 기준으로도 정렬해줘야 함

cnt=1
last=arr[0][1]
for i in range(1,n):
    if arr[i][0]>=last:
        cnt+=1
        last=arr[i][1]

print(cnt)
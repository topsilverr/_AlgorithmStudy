n=int(input())
arr=list(map(int,input().split())) # 배열로 저장

arr.sort() # 오름차순 정렬
res=0
buf=0
for i in arr:
    buf=buf+i
    res=res+buf

print(res)
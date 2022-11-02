n= int(input())
list=list(map(int,input().split()))

d=[0]*100
d[0]=list[0]
d[1]=max(list[0],list[1])
for i in range(2,n):
    d[i]=max(d[i-1],d[i-2]+list[i])

print(d[n-1])
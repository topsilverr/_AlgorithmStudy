n=int(input())

arr=[]
for i in range(n):
    buf=input().split()
    arr.append((buf[0],int(buf[1])))

print(arr)
arr=sorted(arr,key=lambda student:student[1])

for i in arr:
    print(i[0],end=' ')
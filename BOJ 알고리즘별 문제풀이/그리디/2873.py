n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))

arr.sort()
res=0
minus=[]
zero=0
plus=[]
for num in arr:
    if num < 0:
        minus.append(num)
    elif num==0:
        zero+=1
    else:
        plus.append(num)


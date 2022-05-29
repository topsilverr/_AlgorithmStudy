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

plus.sort(reverse=True)
if len(plus)!=0:
    for p in range(len(plus)):
        if len(plus)==1:
            res+=arr[p]
        else:
            res+=max((arr[p]+arr[p+1]),(arr[p]*arr[p+1]))
            del arr[p]
            del arr[p+1]
            p+=2


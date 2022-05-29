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
            res+=plus[p]
        else:
            res+=max((plus[p]+plus[p+1]),(plus[p]*plus[p+1]))
            del plus[p]
            del plus[p+1]
            p+=2

if len(minus)>=2:
    for i in range(len(minus)):
        res+=(minus[i]*minus[i+1])
        i+=2

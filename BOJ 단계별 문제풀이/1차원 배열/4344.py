c=int(input())

for i in range(c):

    arr=list(map(int,input().split()))
    num=arr[0]
    del arr[0]
    avg=sum(arr)/num
    cnt=0
    for a in arr:
        if a>avg:
            cnt=cnt+1

    perc=(cnt/num)*100
    perc=round(perc,3)
    print("{:.3f}%".format(perc))
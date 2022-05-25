def oven(h,m,s):
    H=s//60
    M=s%60

    if h+H>23:
        h=(h+H)-24
        if m+M>59:
            m=(m+M)-60
            h=h+1
        else:
            m=m+M
    else:
        h=h+H
        if m+M>59:
            m=(m+M)-60
            h=h+1
        else:
            m=m+M

    if h==24:
        h=0
    if m==60:
        m=0
    print(h,m)

h,m=map(int,input().split())
s=int(input())
oven(h,m,s)

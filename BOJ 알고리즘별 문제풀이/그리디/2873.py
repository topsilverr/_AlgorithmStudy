r,c=map(int,input().split())

row=[]
res=""
for i in range(r):
    buf=list(map(int,input().split()))
    row.append(buf)

if r%2!=0 & c%2==0:
    for i in range(r//2):
        res+="R"*(c-1)
        res+="D"
        res+="L"*(c-1)
        res+="D"
    res+="R"*(c-1)
elif c%2!=0:
    for i in range(c//2):
        res+="D"*(r-1)
        res+="R"
        res+="U"*(r-1)
        res+="R"
    res+="D"*(r-1)

elif r%2==0 & c%2==0:
    min=1000
    pick=[-1,-1]
    for i in range(r):
        if c%2==0: # 홀수행일때 (row 가 0부터 시작)
            for j in range(1,c,2):
                if row[i][j]<min:
                    pick=[i,j]
                    min=row[i][j]
        else:
            for j in range(0,c,2):
                if row[i][j]<min:
                    pick=[i,j]
                    min=row[i][j]



print(res)
print(pick)
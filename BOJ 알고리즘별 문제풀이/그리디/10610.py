n=list(input())
n.sort(reverse=True)
ans=0

if '0' not in n:
    print(-1)
else:
    for i in n:
        ans+=int(i)
    if ans%3!=0:
        print(-1)
    else:
        print(''.join(n))
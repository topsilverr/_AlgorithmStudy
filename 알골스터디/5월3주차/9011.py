T = int(input())

for _ in range(T):
    n = int(input())
    num = []
    num = list(map(int,input().split()))

    chk = True
    use = [num[n-1]+1]
    res = [0 for _ in range(n)]
    res[-1] = num[n-1]+1

    for i in range(n-2,-1,-1):
        buf = num[i]+1
        use.sort()
        for j in use:
            if buf >= j: # 제일 작은거부터 비교하기 위해서 ( sort 안하면 작은게 있는데 걍 break 될 수 있음 )
                buf += 1
            else:
                break
        if buf > n:
            chk = False
            break # 여기서 break => for i in range(n-2,-1,-1) 을 탈출
        res[i] = buf
        use.append(buf)

    if chk:
        for r in res:
            print(r,end=' ')
    else:
        print("IMPOSSIBLE")


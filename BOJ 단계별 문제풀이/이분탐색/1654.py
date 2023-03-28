def bin_search(arr,target,start,end):
    res = 0
    while start <= end :
        mid = (start+end) // 2
        cnt = 0
        for l in arr :
            cnt += l // mid
        if cnt >= target:
            res = mid
            start = mid + 1
        else:
            end = mid - 1
    return res



k,n = map(int,input().split())
s=[]
for i in range(k):
    s.append(int(input()))

s.sort(reverse=True)

print(bin_search(s,n,1,s[0]))

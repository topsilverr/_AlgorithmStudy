def bin_search(arr,target,start,end):
    while start <= end :
        mid = (start+end) // 2
        res = 0
        for l in arr :
            res += l // mid
        if res >= target:
            start = mid + 1
        else:
            end = mid - 1
    return end



k,n = map(int,input().split())
s=[]
for i in range(k):
    s.append(int(input()))

s.sort(reverse=True)

print(bin_search(s,n,1,s[0]))

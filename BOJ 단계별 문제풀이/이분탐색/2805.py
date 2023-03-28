def bin_search(arr,target,start,end):
    res = 0
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for t in arr:
            if t-mid >= 0:
                cnt = cnt+(t-mid)
        if target >= cnt :
            end = mid - 1
        else:
            res = mid
            start = mid + 1
    return res


n,m = map(int,input().split())
tree = list(map(int,input().split()))


print(bin_search(tree,m,0,max(tree)))

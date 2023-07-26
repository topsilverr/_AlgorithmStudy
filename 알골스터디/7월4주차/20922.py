import sys


input = sys.stdin.readline

arr = []
n, k = map(int, input().split())
arr = list(map(int, input().split()))
counter = [0] * (max(arr) + 1)

l, r = 0, 0

cnt = 0
buf_cnt = 0
buf_arr = []
while r < n:
    if counter[arr[r]] < k:
        counter[arr[r]]+=1
        buf_arr.append(arr[r])
        r += 1
    else:
        counter[arr[l]] -= 1
        l += 1

    cnt = max(cnt,r-l)

print(cnt)
import sys

input = sys.stdin.readline

n, s = map(int, input().split())

arr = list(map(int, input().split()))

l, r = 0, 0

res = 100001

buf = arr[0]

while True:
    if buf >= s:
        buf -= arr[l]
        buf_res = r - l + 1
        res = min(res, buf_res)
        l += 1

    else:
        r += 1
        if r == n:
            break
        buf += arr[r]

if res == 100001:
    print(0)
else:
    print(res)

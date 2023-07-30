import sys
import math

input = sys.stdin.readline

g = int(input())

l,r = 1, 1
res = []
while l <= r:
    chk = r**2 - l**2
    if r - l == 1 and chk > g:
        break
    if chk < g:
        r += 1
    elif chk > g:
        l += 1
    else:
        res.append(r)
        r+=1

if res:
    for i in range(len(res)):
        print(res[i])
else:
    print(-1)
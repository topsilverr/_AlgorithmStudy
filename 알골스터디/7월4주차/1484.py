import sys
import math

input = sys.stdin.readline

g = int(input())

l,r = 1, 1
res = []
while l <= r:
    chk = r**2 - l**2
    if chk == g:
        res.append(r)
        l += 1
        r = l
    elif chk < g:
        r += 1
    elif chk > g:
        l += 1
        r = l
    elif chk > 100000:
        print(-1)
        break

res.sort()
print(res)
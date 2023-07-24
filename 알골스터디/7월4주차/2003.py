import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

s, e = 0, 0
sums = 0
res = 0
while n >= e >= s:
    buf = a[s:e]
    sums = sum(buf)
    if sums == m:
        res += 1
        s += 1
    elif sums < m:
        e += 1
    else:
        s += 1
print(res)

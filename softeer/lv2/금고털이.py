#그리디,,
import sys
input = sys.stdin.readline

w,n = map(int,input().split())
s = []
for i in range(n):
    s.append(list(map(int,input().split())))

s.sort(key = lambda x:x[1], reverse=True)

res = 0

for m,p in s:
    if w-m>=0:
        w-=m
        res+=m*p
    else:
        res+=w*p
        break
print(res)
from collections import deque

n,k = map(int,input().split())

num = deque()
res = []
for i in range(1,n+1):
    num.append(i)

while num:
    for _ in range(k-1):
        num.append(num.popleft())
    res.append(num.popleft())

print('<' + ', '.join(map(str, res)) + '>')

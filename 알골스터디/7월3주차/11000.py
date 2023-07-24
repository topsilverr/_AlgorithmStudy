import sys

input = sys.stdin.readline

n = int(input())

cls = []
res = []

for _ in range(n):
    cls.append(list(map(int, input().split())))

cls.sort(key=lambda x: x[0])
cls.sort(key=lambda x: x[1])

buf = cls[0][1]
res_li = []

res = 1

for i in range(1, n):
    if buf <= cls[i][0]:
        buf = cls[i][1]
        res_li.append(cls[i][1])
    else:
        res += 1
        buf = cls[i][1]
print(res)


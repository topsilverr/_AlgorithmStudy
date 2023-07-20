import sys

input = sys.stdin.readline

n = int(input())

time = []
res = 1 # 시작 회의 이미 지정

for _ in range(n):
    time.append(list(map(int,input().split())))

time.sort(key = lambda x:x[0])
time.sort(key = lambda x:x[1])

std = time[0][1]
for i in range(1,n):
    if time[i][0] >= std:
        res += 1
        std = time[i][1]

print(res)

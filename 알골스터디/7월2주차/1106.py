import sys

input = sys.stdin.readline

city = []
c,n = map(int,input().split())

dp = [0 for _ in range(c+100)]

for _ in range(n):
    city.append(list(map(int,input().split())))


# 3 5
# 1 1

for n,nn in city:
    for i in range(nn,c+100):
        dp[i] = min(dp[i-nn]+n,dp[i])


print(min(dp[c:]))




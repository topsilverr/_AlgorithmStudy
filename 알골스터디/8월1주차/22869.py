import sys

input = sys.stdin.readline

n,k = map(int,input().split())
rocks = [0] + list(map(int,input().split()))

chk = 1
res = 1001

dp = [-1] * (n+1)
dp[1] = 1

for i in range(1,n+1):
    if dp[i] == -1:
        continue
    for j in range(i+1,n+1):
        if (j-i) * (1+abs(rocks[i]-rocks[j])) <= k:
            dp[j] = 1
    if dp[n] == 1:
        print("YES")
        break

if dp[n] == -1:
    print("NO")

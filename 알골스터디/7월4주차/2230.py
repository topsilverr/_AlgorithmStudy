import sys

input = sys.stdin.readline

nums = []

n,m = map(int,input().split())
for _ in range(n):
    nums.append(int(input()))
nums.sort()

l,r = 0, 0
res = 2000000000

while r < n and l < n:
    # print(nums[l], nums[r])
    if nums[r] - nums[l] >= m:
        # print(abs(nums[r]-nums[l]))
        res = min(nums[r]-nums[l],res)
        l += 1
    elif nums[r] - nums[l] < m:
        r += 1


print(res)
#돌면서 min 값 찾기
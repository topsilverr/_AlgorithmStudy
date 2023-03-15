from collections import Counter

M = int(input())
card = list(map(int,input().split()))
N = int(input())
nums = list(map(int,input().split()))

counter = Counter(card)
res=[]
for i in nums:
    res.append(counter[i])

print(*res)
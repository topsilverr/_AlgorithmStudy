import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    res = 0
    while True:
        max_num = max(nums)
        num_index = nums.index(max_num)
        res+=(max_num*num_index) - sum(nums[:num_index])

        if num_index == len(nums) - 1:
            break
        nums = nums[num_index+1:]
    print("#"+str(i+1),res)


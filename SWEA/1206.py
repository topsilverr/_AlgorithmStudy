import sys
sys.stdin = open("input.txt","r")

for i in range(1,11):
    n = int(input())
    nums = list(map(int,input().split()))
    res = 0
    for b in range(2,len(nums)-1):
        if nums[b]<=nums[b-1] or nums[b]<=nums[b-2] or nums[b]<=nums[b+1] or nums[b]<=nums[b+2]:
            res+=0
        else:
            buf_list = [nums[b-1],nums[b-2],nums[b+1],nums[b+2]]

            max_b = max(buf_list)
            res += nums[b]-max_b
    print("#"+str(i),res)


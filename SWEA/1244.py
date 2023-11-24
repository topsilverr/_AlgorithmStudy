import sys
sys.stdin=open("input.txt","r")

t = int(input())

for test_case in range(1,t+1):
    num,chance=map(int,input().split())
    nums = []
    for i in str(num):
        nums.append(int(i))

import sys
sys.stdin = open("input.txt","r")
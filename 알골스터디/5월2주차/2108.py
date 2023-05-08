from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())

num = []

for i in range(n):
    num.append(int(input()))

def mean():
    res = sum(num)
    return round(res/n)

def median():
    num.sort()
    med_idx=len(num)//2
    return num[med_idx]

def common():
    dict = Counter(num)
    comm=dict.most_common()
    if len(comm)>1 and comm[0][1] == comm[1][1]:
        return comm[1][0]
    else:
        return comm[0][0]

print(mean())
print(median())
print(common())
print(max(num)-min(num))
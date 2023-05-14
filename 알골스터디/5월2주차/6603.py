from itertools import combinations
import sys
while True:
    num = list(map(int,sys.stdin.readline().split()))
    if num[0] == 0:
        break
    tot = num.pop(0)

    res = combinations(num,6)
    for i in res:
        buf = list(map(str,i))
        print(" ".join(buf))
    print()
# 셀프넘버가 아닌 것 구해서 제거

nonSelfNum = []


for num in range(1,10001):
    num = num + sum(map(int,str(num)))
    nonSelfNum.append(num)

for selfNum in range(1,10001):
    if selfNum not in nonSelfNum:
        print(selfNum)
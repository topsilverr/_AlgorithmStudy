n = int(input())

stack = []
res = []

now = 1
chk = True

for i in range(n):
    num = int(input()) # 이런거 어케 생각하지
    while now <= num:
        stack.append(now)
        res.append('+')
        now+=1
    if stack[-1] == num:
        stack.pop()
        res.append('-')
    else:
        chk = False

if chk:
    for j in res:
        print(j)
else:
    print("NO")

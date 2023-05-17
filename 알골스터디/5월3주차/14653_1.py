n,k,q = map(int,input().split())

chat = []
for _ in range(k):
    r,p = input().split()
    chat.append([int(r),p])

part = [] # 참여자 목록
for i in range(1,n):
    part.append(chr(ord('A')+i))

target = q-1
tar_state = chat[target][0]
start_idx = -1

for i in range(target):
    if chat[i][0] == tar_state and i != target:
        start_idx = i
        break
#
print(start_idx)
if start_idx != -1:
    for i in range(start_idx,len(chat)):
        if chat[i][1] in part:
            part.remove(chat[i][1])
else:
    for i in range(target,len(chat)):
        if chat[i][1] in part:
            part.remove(chat[i][1])

if len(part) == 0:
    print(-1)
else:
    for i in range(len(part)):
        print(part[i],end=' ')
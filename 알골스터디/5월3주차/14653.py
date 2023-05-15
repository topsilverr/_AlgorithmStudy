n,k,q = map(int,input().split())

chat = []
for _ in range(k):
    r,p = input().split()
    chat.append([int(r),p])

tar_idx = q-1 # 원하는 메세지 인덱스

part = [] # 참여자 목록
for i in range(1,n):
    part.append(chr(ord('A')+i)) # 본인, 즉 A 일단 빼고, 보낸 사람도 빼고 만들어야되나?


if chat[tar_idx][0] <= n-1:# 나만 보낼 수 있는게 아니구나! 나랑 보낸 사람둘다 빼줘야됨 근데 나는 이미 빠져있으니가,,,
    for p in range(tar_idx,len(chat)):
        if chat[p][1] in part:
            part.remove(chat[p][1])
    i = tar_idx
    while i >= 1:
        if chat[i][0] == chat[i - 1][0]:
            if chat[i - 1][1] in part:
                part.remove(chat[i - 1][1])
            i -= 1
        else:
            break

# i = tar_idx
# while i >= 1:
#     if chat[i][0] == chat[i - 1][0]:
#         if chat[i-1][1] in part:
#             part.remove(chat[i - 1][1])
#         i -= 1
#     else:
#         break

# for i in range(tar_idx - 1, -1, -1):
#     if chat[i][0] == chat[tar_idx][0]:
#         if chat[i][1] in part:
#             part.remove(chat[i][1])

if len(part) == 0:
    print(-1)
else:
    for i in range(len(part)):
        print(part[i],end=' ')



# 5명 -> 4 : 한명도 안 읽은거

# 5 6 4
# 1 A
# 2 A
# 2 A
# 3 A -> 여기서 안 읽은 사람 누구?
#        if n-1 보다 적으면 :
#             뒤에서 메시지 보낸 기록이 있는 사람은 읽은거
#        elif n-1 이면 :
#            다 안읽은거
#
# 3 B
# 3 A
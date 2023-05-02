n = int(input())

cnt = 0
chk = []
now = ''
for i in range(n):
    chk = []
    word = input()
    tag = True
    now = word[0]
    chk.append(word[0])
    for w in word[1:]:
        if w != now and w not in chk:
            chk.append(w)
        elif w == now and w in chk and w != chk[-1]:
            tag = False
            break
        elif w != now and w in chk:
            tag = False
            break
        # elif w == now and w not in chk:
            # chk.append(w)
        now = w

    if tag:
        cnt+=1

print(cnt)
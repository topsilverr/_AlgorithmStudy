n = int(input())
dic = {}
buf = []


for i in range(n):
    buf.append(list(input().split()))
    dic[buf[i][0]] = [buf[i][1],buf[i][2]]

def pre_traverse(now):
    if now != '.':
        print(now,end='')
        pre_traverse(dic[now][0])
        pre_traverse(dic[now][1])

def in_traverse(now):
    if now != '.':
        in_traverse(dic[now][0])
        print(now,end='')
        in_traverse(dic[now][1])

def post_traverse(now):
    if now != '.':
        post_traverse(dic[now][0])
        post_traverse(dic[now][1])
        print(now,end='')

pre_traverse('A')
print()
in_traverse('A')
print()
post_traverse('A')

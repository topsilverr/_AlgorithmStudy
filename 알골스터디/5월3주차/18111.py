n,m,b = map(int,input().split())

rand = []
for i in range(n):
    rand.append(list(map(int,input().split())))
print(rand)

# 다 돌면서 제일 작은 큰 값 작은값 찾기
# 큰값이랑 땅 비교하면서 인벤토리에서 꺼내써야할 개수랑 깎을 블럭 개수 확인
max = 0
min = 257
min_idx = [0,0]
max_idx = [0,0]

for i in range(n):
    for j in range(m):
        if rand[i][j] <= min:
            min = rand[i][j]
            min_idx.append([i,j])
        if rand[i][j] >= max:
            max = rand[i][j]
            max_idx.append(([i,j]))
print(min,max)
# 쌓는게 더 적게 걸리니까
# 최댓값이랑 비교

cnt = 0

for i in range(n):
    for j in range(m):
        if rand[i][j] != max:
            gap = max - rand[i][j]
            cnt += gap
cnt_s = 0
if cnt > b: # 깎는거 선택
    print("깎기")
    for i in range(n):
        for j in range(m):
            if rand[i][j] != min:
                gap = rand[i][j] - min
                cnt_s += 2*gap
                b+=gap


print(min(cnt,cnt_s))
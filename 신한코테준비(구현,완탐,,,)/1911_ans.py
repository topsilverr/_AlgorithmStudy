n, l = map(int, input().split()) # 웅덩이 개수, 널빤지 길이
pond = [tuple(map(int, input().split())) for _ in range(n)]
pond.sort(key= lambda x: (x[0],x[1]))
point = pond[0][0] # 널빤지 이어붙이고 끝자락을 변수 point로 둘 것이다. 초기에는 널빤지를 둔 곳이 없으므로 시작해야할 포인트로 변수를 잡는다.
cnt = 0
for start, end in pond:
    if point > end:
        continue
    elif point < start:
        point= start
    dist = end - point
    print("dist :", dist)
    r = 1
    if dist % l ==0:
        r = 0
    count = dist//l + r
    print("count :", count)
    point += count*l # 시작점에서 널빤지를 이어붙이고 마지막 끝자락
    print("point :", point)
    cnt += count
print(cnt)
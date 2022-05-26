n=list(input()) # 문자열로 받기
n.sort(reverse=True) # 내림차순 정렬 왜? 만들 수 있는 수 중에서 제일 큰 수를 출력해야되니까
ans=0

if '0' not in n: # 0이 없으면 30의 배수 될 수 없음
    print(-1)
else:
    for i in n:
        ans+=int(i)
    if ans%3!=0: # 3의 배수 조건 => 모든 자리수의 합이 3의 배수
        print(-1)
    else:
        print(''.join(n)) # 공백없이 배열 조인해서 출력
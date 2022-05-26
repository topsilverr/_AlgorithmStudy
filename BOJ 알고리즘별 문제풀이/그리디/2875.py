n,m,k=map(int,input().split())

a=n//2
# 여자로만 만든 팀에 남자 분배
if m>a:
    m=m-n//2
    n=0
else:
    a=m
    m=0
    n=n-(2*a)

buf=n+m # 팀을 만들고 남은 수

if k>buf: # 남은 수가 인턴십에 참가해야되는 학생 수보다 적으면 팀을 해체해야됨
    res=k-buf
    if res%3!=0:
        a=a-((res//3)+1)
    else:
        a=a-(res//3)


print(a)
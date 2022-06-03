n=int(input())

res=0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h)+str(m)+str(s): # 숫자를 문자열로 변경하여 3이 있는 시각 개수 세기
                res+=1

print(res)
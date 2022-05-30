n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input())) # 일단 숫자 리스트로 받기

arr.sort() # 오름차순으로 정렬
res=0 # 최종 결과값 저장 변수
minus=[] # 0과 음수를 담을 리스트
plus=[] # 양수를 담을 리스트
for num in arr:
    if num <= 0:
        minus.append(num)
    elif num==1: # 원래는 0을 기준으로 함 ( 0은 음수랑 곱하면 사라지니까 기준으로 해야될 것 같았음,,,) 근데 1을 기준으로 해야됨 ( 1은 곱셈을 하면 최댓값이 나오지 않기 때문에 따로 더해줌 )
        res+=1
    else:
        plus.append(num)

plus.sort(reverse=True) # 가장 큰 수를 곱해주기 위해 내림차순으로 정렬


if len(plus)%2==0: # 양수의 개수가 짝수인 경우, 내림차순으로 정렬된 숫자를 둘둘씩 곱하여 더해줌
    for p in range(0,len(plus),2):
        res+=plus[p]*plus[p+1]
else: # 홀수면, 가장 큰 수부터 두개씩 곱한 후, 가장 작은 수는 따로 더해주어야 최대값이 나옴
    for p in range(0,len(plus)-1,2):
        res += plus[p] * plus[p + 1]
    res+=plus[len(plus)-1]

if len(minus)%2==0: # 음수의 개수가 짝수인 경우, 오름차순으로 정렬된 숫자를 둘둘씩 곱하여 더해줌 (음수끼리 곱하면 양수가 나옴)
    for m in range(0,len(minus),2):
        res+=minus[m]*minus[m+1]
else: # 홀수면, 가장 작은 수부터 두개씩 곱한 후, 가장 큰 수는 따로 더해주어야 최대값이 나옴
    for m in range(0,len(minus)-1,2):
        res += minus[m] * minus[m + 1]
    res+=minus[len(minus)-1]

print(res)
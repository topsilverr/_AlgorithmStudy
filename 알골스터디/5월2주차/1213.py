from collections import Counter

name = list(input())
# 문자열 배열로 변환하기,,, 기억해!

r_name = []
odd = 0
odd_alp = ''
res_f = ''
res = ''

name.sort()
c_dic = Counter(name)

for i in c_dic:
    if c_dic[i] % 2 != 0:
        odd_alp = i
        odd += 1

if odd > 1:
    print("I'm Sorry Hansoo")
else:
    for alp, num in c_dic.items():
        res_f += (alp * (num // 2))

    res = res_f + odd_alp + res_f[::-1]
    print(res)





# 알파벳을 일단 정렬
#
# <홀수 없는 경우>
# 걍 앞에서부터 반띵해서 앞뒤로 넣기


# <홀수가 1개 있는경우>
# 홀수의 위치
# 홀수인 값이 마지막이 아닌 경우엔 그냥 하나만 가운데 넣고 나머지는 앞뒤로 배분
#
# -> 제일 앞 알파벳이 홀수일 경우
#     총 길이의 가운데에 해당 알파벳 한개 넣고 나머지 이등분해서 앞뒤에 같은 수로 넣기
#     그 뒤로는 다 짝수 => 이등분해서 앞뒤로 같은 수로 넣기
# -> 제일 앞 알파벳이 짝수일 경우
#     이등분해서 앞뒤로 같은 수로 넣고
#     홀수인 값이 마지막 값이면 걍 가운데 때려넣고
#     마지막 값이 아니면 인덱스 가운데에 그 값 하나 넣고 나머지 이등분해서 앞뒤로 분배
#     => 마지막값인지 아닌지는 key값 개수와 현재 for 문이 몇번째인지 비교?

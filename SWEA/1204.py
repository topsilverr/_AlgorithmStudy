from collections import Counter

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    nums = list(map(int,input().split()))

    res = Counter(nums)
    ans = res.most_common()
    max_cnt = ans[0][1]
    buf = []
    buf.append(ans[0][0])
    for cnt in ans:
        if cnt[1] == max_cnt:
            buf.append(cnt[0])
        else:
            break
    res = max(buf)

    print("#"+str(n),res)
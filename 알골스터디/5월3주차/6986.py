import sys
input = sys.stdin.readline
n,k = map(int,input().split())

score = []
score_buf = []
for i in range(n):
    score.append(float(input()))

score.sort()

def delete(n,k):

    score_buf = score[k:-k]
    return score_buf

def trans(n,k):
    for i in range(0,k):
        score[i] = score[k]
    for j in range(n-k,n):
        score[j] = score[n-k-1]
    return score

if k == 0:
    print('{:.2f}'.format(sum(score) / len(score) + 0.00000001))
    print('{:.2f}'.format(sum(score) / len(score) + 0.00000001))
else:
    cut=delete(n,k)
    print('{:.2f}'.format(sum(cut)/len(cut)+ 0.00000001))
    cor=trans(n,k)
    print('{:.2f}'.format(sum(cor)/len(cor)+ 0.00000001))
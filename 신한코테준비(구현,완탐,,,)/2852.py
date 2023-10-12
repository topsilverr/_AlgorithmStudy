n = int(input())

a_win = 0
b_win = 0
a_tmp = 0
b_tmp = 0
chk = 0

for i in range(n):
    team,time = input().split()
    m,s = map(int,time.split(':'))
    t = 60*m+s
    if team =='1':
        if chk == 0:
            chk+=1
            a_tmp = t
        else:
            chk+=1


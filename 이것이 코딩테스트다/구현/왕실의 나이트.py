buf=input()
x=int(ord(buf[0]))-int(ord('a'))+1 # 알파벳을 숫자로 바꾸기
y=int(buf[1])
now=[x,y]
arr=[[False for x in range(1,10)]for y in range(1,10)] # 최대로 빠져나갈 수 있는 칸 2칸 이므로 10칸까지 false로 설정

for i in range(1,9): # 주어진 체스판에 해당하는 칸은 true로 변경
    for j in range(1,9):
        arr[i][j]=True

cnt=0
#모든 경우의 수에 대하여 해당 여부 확인
if arr[x + 2][y - 1]:
    cnt+=1
if arr[x+2][y+1]:
    cnt+=1
if arr[x+1][y-2]:
    cnt+=1
if arr[x-1][y-2]:
    cnt+=1
if arr[x - 2][y - 1]:
    cnt+=1
if arr[x - 2][y + 1]:
    cnt+=1
if arr[x + 1][y + 2]:
    cnt+=1
if arr[x - 1][y + 2]:
    cnt+=1

print(cnt)
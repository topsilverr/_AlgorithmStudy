n = int(input())

switch = list(map(int,input().split()))

s = int(input())

s_list = []
for i in range(s):
    s_list.append(list(map(int,input().split())))

for stud in s_list:
    if stud[0] == 1:
        i = 1
        for j in range(len(switch)):
            if j+1 == i*stud[1]:
                if switch[j] == 1:
                    switch[j] = 0
                else:
                    switch[j] = 1
                i+=1
    if stud[0] == 2:
        mid = stud[1]-1
        if switch[mid] == 1:
            switch[mid] = 0
        else:
            switch[mid] = 1
        l = mid - 1
        r = mid + 1
        while l >= 0 and r < len(switch) :
            if switch[l] == switch[r] :
                if switch[l] == 1:
                    switch[l] = 0
                    switch[r] = 0
                else:
                    switch[l] = 1
                    switch[r] = 1
                l -= 1
                r += 1
            else:
                break


for i in range(n):
    print(switch[i], end = " ")
    if i % 20 == 19 :
        print()



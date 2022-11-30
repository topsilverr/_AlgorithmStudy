members=["A","B"]
commands=[["W","MY","1"],["W","A","7"],["W","B","4"],["W","MY","9"],["W","A","11"],["W","A","18"],["R","B",""]]
messageID="11"

total=1+len(members)
read=[]
for i in commands:
    if i[2]==messageID:
        idx=commands.index(i)
        read.append(i[1])

buf=commands[idx+1:]
for j in buf:
    for k in read:
        if j[1] != k:
            print(j[1])
            read.append(j[1])
            break
        break

answer=total-len(read)
print(answer)

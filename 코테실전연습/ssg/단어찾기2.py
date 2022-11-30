dictionary = ["popop", "abab", "dsfsdfs", "serwerwe", "werwerwer", "dfdfderwer","abee","abeef"]
command = [["lengthMatch","@@ab"]]

for i in command:
    answer = []
    if i[1][0]=='@':
        i.append("postfix")
    elif i[1][2]=='@':
        i.append("prefix")
    if i[2]=="prefix":
        for j in dictionary:
            if j[0:2] == i[1][0:2] and len(j)==4:
                answer.append(j)
                dictionary = answer
    if i[2]=="postfix":
        for j in dictionary:
            if j[2:4] == i[1][2:4] and len(j)==4:
                answer.append(j)
                dictionary = answer
print(answer)

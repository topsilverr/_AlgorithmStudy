dictionary = ["popop", "abcd", "dsfsdfs", "serwerwe", "werwerwer", "dfdfderwer","abee","abeef"]
command = [["postfix", "wer"], ["prefix", "dfd"]]

for i in command:
    answer = []
    if i[0] == "postfix":
        length = len(i[1])
        for j in dictionary:
            if j[len(j) - length:] == i[1]:
                answer.append(j)
                dictionary = answer
    if i[0] == "prefix":
        length = len(i[1])
        for j in dictionary:
            if j[0:length] == i[1]:
                answer.append(j)
                dictionary = answer
print(answer)



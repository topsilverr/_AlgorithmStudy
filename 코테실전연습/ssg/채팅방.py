def solution(members, commands, messageIDs):
    answer = []
    res = []
    read = []
    for i in commands:
        if i[0] == 'W' and i[1] == 'MY':
            res = read
            read = []
        elif i[0] == 'W' and i[1] != 'MY':
            read.append(i[2])
        elif i[0] == 'R' and i[1] == 'MY':
            res = read
            read = []
        elif i[0] == 'R' and i[1] != 'MY':
            res = res

    for j in messageIDs:
        if j in res:
            answer.append(True)
        else:
            answer.append(False)
    return answer
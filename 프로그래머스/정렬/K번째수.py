def solution(array, commands):
    answer = []
    for cmd in commands:
        buf = array[cmd[0] - 1:cmd[1]]
        buf.sort()
        answer.append(buf[cmd[2] - 1])

    return answer
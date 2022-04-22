def score(a):
    if 90<=a<=100:
        return "A"
    elif 80<=a<=89:
        return "B"
    elif 70<=a<=79:
        return "C"
    elif 60<=a<=69:
        return "D"
    return "F"

a=int(input())
print(score(a))
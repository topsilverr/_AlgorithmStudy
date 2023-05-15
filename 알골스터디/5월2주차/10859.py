import math
n = input()



def is_prime_number(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    m = int(x ** 0.5) + 1
    for i in range(3, m, 2):
        if x % i == 0:
            return False
        i += 2
    return True


def reverse(n):
    reverse_n = ""
    for p in n:
        if p == '0' or p == '2' or p == '5' or p == '8' or p == '1':
            reverse_n+=p
        elif p =='6':
            reverse_n+='9'
        elif p == '9':
            reverse_n+='6'
        else:
            return False
    reverse = reverse_n[::-1]
    return reverse

if(is_prime_number(int(n))):
    res = reverse(n)
    if (res):
        res = int(res)
        if (is_prime_number(res)):
            print("yes")
        else:
            print("no")
    else:
        print("no")
else:
    print("no")

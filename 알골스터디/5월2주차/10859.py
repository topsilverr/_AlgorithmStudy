import math
n = int(input())
n_list = list(str(n))

reverse_n = []

def is_prime_number(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
    return True


def reverse(n_list):
    for p in n_list:
        if p == '0' or p == '2' or p == '5' or p == '8':
            reverse_n.append(p)
        elif p == '1':
            reverse_n.append(p)
        elif p =='6':
            reverse_n.append('9')
        elif p == '9':
            reverse_n.append('6')
        else:
            print('no')
    reverse = reverse_n[::-1]
    return reverse

if(is_prime_number(n)):
    res = reverse(n_list)
    if (res):
        res = ''.join(res)
        reverse_int = int(res)
        if (is_prime_number(reverse_int)):
            print("yes")
        else:
            print("no")
else:
    print("no")

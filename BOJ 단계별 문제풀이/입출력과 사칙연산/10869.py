def solve(a, b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(int(a / b))
    print(a % b)


if __name__ == '__main__':
    a, b = map(int, input().split())
    solve(a, b)

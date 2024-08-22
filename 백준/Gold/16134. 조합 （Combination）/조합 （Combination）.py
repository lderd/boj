def hose2(b):
    a = 1000000007
    s = [1, 0]
    t = [0, 1]
    while a > 0 and b > 0:
        if a >= b:
            q = a // b
            a %= b
        else:
            q = b // a
            b %= a
        s = [s[1], s[0] - s[1] * q]
        t = [t[1], t[0] - t[1] * q]
    return t[0]

n, r = map(int, input().split())
answer = 1
div = 1000000007
for i in range(r+1, n + 1):
    answer *= i
    answer %= div
tmp = 1
for i in range(1, n - r + 1):
    tmp *= hose2(i) + div
    tmp %= div
print((answer * tmp) % div)
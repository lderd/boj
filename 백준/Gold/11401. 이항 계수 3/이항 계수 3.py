def find(number):
    a = m
    b = number
    s = (1, 0)
    t = (0, 1)
    while True:
        if a <= 1 or b <= 1:
            break
        if a >= b:
            q = a // b
            a = a % b
        else:
            q = b // a
            b = b % a
        s = (s[1], s[0] - s[1] * q)
        t = (t[1], t[0] - t[1] * q)
    return t[1] if (t[1] > 0) else t[1] + m


n, k = map(int, input().split())
answer = 1
m = 1000000007
for num in range(max(k + 1, 1), n + 1):
    answer = (answer * num) % m
for num in range(2, n - k + 1):
    answer = (answer * find(num)) % m
print(answer)
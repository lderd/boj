from bisect import bisect_left
n = int(input())
A = (n - 1 - (n // 2)) * (n // 2)
B = 0
C = 0
prime = set(list(range(2, n+1)))
divisor = set()
divisor.add(1)
divisor.add(n)
for i in range(2, n//2+1):
    for j in range(i, n//2+1):
        if i * j > n:
            break
        if i * j == n:
            divisor.add(i)
            divisor.add(j)
        if i * j in prime:
            prime.remove(i * j)
divisor = sorted(list(divisor))
prime = sorted(list(prime))
divisor_len = len(divisor)
prime_len = len(prime)
x = y = 0
while x < divisor_len and divisor[x] <= n // 2:
    y = x
    while y < divisor_len - 1:
        if divisor[x] + divisor[y] > n:
            break
        z_index = bisect_left(divisor, divisor[x] + divisor[y])
        if z_index < divisor_len and divisor[z_index] == divisor[x] + divisor[y]:
            B += 1
        y += 1
    x += 1
'''
Z가 소수가 되어야 하기에 Z >= 5의 홀수
인데 소수는 2를 제외하면 모두 홀수이다.
홀수 + 홀수 = 짝수 이다
따라서 X는 반드시 2가 되어야 한다
'''
y = 1
while y < prime_len - 1:
    if 2 + prime[y] > n:
        break
    if prime[y] + 2 == prime[y+1]:
        C += 1
    y += 1
print(A)
print(B)
print(C)
import sys
input = sys.stdin.readline
n, q = map(int, input().split())
a = sorted(map(int, input().split()))
b = [0] * (n+1)
for i in range(n):
    num = a[i]
    i += 1
    while i <= n:
        b[i] += num
        i += i & -i
for _ in range(q):
    l, r = map(int, input().split())
    answer = 0
    while r > 0:
        answer += b[r]
        r -= r & -r
    l -= 1
    while l > 0:
        answer -= b[l]
        l -= l & -l
    print(answer)
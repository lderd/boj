import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
tree = [0] * (n+1)
for i in range(1, n+1):
    num = int(input())
    while i <= n:
        tree[i] += num
        i += i & -i
idx_change = [0] * (n+1)
change = [0] * (n+1)
for _ in range(m+k):
    a, b, c, *d = map(int, input().split())
    if a == 1:
        d = d[0]
        idx = b
        while idx <= n:
            idx_change[idx] += d
            change[idx] += d * (-b+1)
            idx += idx & -idx
        idx = c + 1
        while idx <= n:
            idx_change[idx] -= d
            change[idx] -= d * (-c)
            idx += idx & -idx
    else:
        answer = 0
        mul = 0
        idx = c
        while idx > 0:
            mul += idx_change[idx]
            answer += tree[idx] + change[idx]
            idx -= idx & -idx
        answer += c * mul
        mul = 0
        idx = b - 1
        while idx > 0:
            mul += idx_change[idx]
            answer -= tree[idx] + change[idx]
            idx -= idx & -idx
        answer -= mul * (b-1)
        print(answer)
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = [0] * (n + 1)
tree = [0] * (n + 1)
for i in range(1, n+1):
    num = int(input())
    idx = i
    arr[idx] = num
    while idx <= n:
        tree[idx] += num
        idx += idx & -idx
for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        idx = b
        gap = c - arr[idx]
        while idx <= n:
            tree[idx] += gap
            idx += idx & -idx
        arr[b] += gap
    elif a == 2:
        tmp = 0
        idx = c
        while idx > 0:
            tmp += tree[idx]
            idx -= idx & -idx
        idx = b - 1
        while idx > 0:
            tmp -= tree[idx]
            idx -= idx & -idx
        print(tmp)
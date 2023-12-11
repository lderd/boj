import sys
input = sys.stdin.readline
n = int(input())
a = [int(input()) for _ in range(n)]
tmp = [0] * n
for i in range(n):
    if i == 0:
        tmp[i] = a[i]
    elif i == 1:
        tmp[i] = a[0] + a[1]
    elif i == 2:
        tmp[i] = max(a[0] + a[1], a[1] + a[2], a[0] + a[2])
    else:
        tmp[i] = max(tmp[i-3] + a[i-1] + a[i], tmp[i-2] + a[i], tmp[i-1])
print(tmp[-1])
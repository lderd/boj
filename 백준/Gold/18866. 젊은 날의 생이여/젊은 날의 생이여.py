import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    u, v = map(int, input().split())
    arr.append((u, v))

#     작은 u, 큰 v, 큰 u, 작은 v
cal = [[int(1e+9)+1, 0, 0, int(1e+9)+1] for _ in range(n)]
for i in range(n):
    u, v = arr[i]
    if u > 0:
        cal[i][0] = u
    if v > 0:
        cal[i][1] = v
    if i > 0:
        cal[i][0] = min(cal[i][0], cal[i-1][0])
        cal[i][1] = max(cal[i][1], cal[i-1][1])
    u, v = arr[-i-1]
    if u > 0:
        cal[-i-1][2] = u
    if v > 0:
        cal[-i-1][3] = v
    if i > 0:
        cal[-i-1][2] = max(cal[-i-1][2], cal[-i][2])
        cal[-i-1][3] = min(cal[-i-1][3], cal[-i][3])
answer = -1
for i in range(n-1):
    a, b, *_ = cal[i]
    *_, c, d = cal[i+1]
    if a > c and b < d:
        answer = i + 1
print(answer)
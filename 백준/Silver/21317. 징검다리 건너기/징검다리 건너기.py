n = int(input())
arr = []
for _ in range(n-1):
    a, b = map(int, input().split())
    arr.append([a, b])
k = int(input())
e = [[0, 0]] + [[1000000] * 2 for _ in range(n-1)]
for i in range(n-1):
    e[i+1][0] = min(e[i+1][0], e[i][0] + arr[i][0])
    e[i+1][1] = min(e[i+1][1], e[i][1] + arr[i][0])
    if i + 2 < n:
        e[i+2][0] = min(e[i+2][0], e[i][0] + arr[i][1])
        e[i+2][1] = min(e[i+2][1], e[i][1] + arr[i][1])
    if i + 3 < n:
        e[i+3][1] = min(e[i+3][1], e[i][0] + k)
print(min(e[n-1]))
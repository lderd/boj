import sys
input = sys.stdin.readline

n = int(input())
near = [[0] for _ in range(n)]
for _ in range(n-1):
    a, b = map(lambda x:int(x) - 1, input().split())
    near[a].append(b)
    near[a][0] += 1
    near[b].append(a)
    near[b][0] += 1
d = 0
g = 0
for i in range(n):
    l = near[i][0]
    if l >= 3:
        g += l * (l - 1) * (l - 2)
    for idx in range(1, near[i][0] + 1):
        daum = near[i][idx]
        d += (l - 1) * (near[daum][0] - 1)
if d > g:
    print('D')
elif d < g:
    print('G')
elif d == g:
    print('DUDUDUNGA')
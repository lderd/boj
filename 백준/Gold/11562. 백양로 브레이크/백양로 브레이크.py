import sys
input = sys.stdin.readline
# 건물 수n, 길의 수m
n, m = map(int, input().split())
cnt = [[999] * n for _ in range(n)]
for _ in range(m):
    u, v, b = map(int ,input().split())
    cnt[u-1][v-1] = 0
    if b:
        cnt[v-1][u-1] = 0
    # 길은 있는데 가지는 못한다
    else:
        cnt[v-1][u-1] = 1
for i in range(n): cnt[i][i] = 0
for k in range(n):
    for i in range(n):
        if k == i: continue
        for j in range(n):
            if k == j or j == i: continue
            cnt[i][j] = min(cnt[i][k] + cnt[k][j], cnt[i][j])
t = int(input())
for _ in range(t):
    s, e = map(int, input().split())
    print(cnt[s-1][e-1])
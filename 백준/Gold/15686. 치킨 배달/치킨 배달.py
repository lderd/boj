from itertools import combinations
n, m = map(int, input().split())
city = [input().split() for _ in range(n)]
home = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == '1':
            home.append((i, j))
        elif city[i][j] == '2':
            chicken.append((i, j))
home_l = len(home)
chicken_l = len(chicken)
chicken_dist = [[0] * chicken_l for _ in range(home_l)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for index in range(chicken_l):
    ci, cj = chicken[index]
    q = [(ci, cj)]
    checked = [[False] * n for _ in range(n)]
    checked[ci][cj] = True
    while q:
        i, j = q.pop()
        for di, dj in d:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and not checked[ni][nj]:
                checked[ni][nj] = True
                q.append((ni, nj))
                if city[ni][nj] == '1':
                    idx = home.index((ni, nj))
                    chicken_dist[idx][index] = abs(ci-ni) + abs(cj-nj)
answer = 13000
for combi in combinations(list(range(chicken_l)), m):
    dist = 0
    for home_idx in range(home_l):
        tmp = 1000
        for chicken_idx in combi:
            tmp = min(tmp, chicken_dist[home_idx][chicken_idx])
        dist += tmp
    answer = min(dist, answer)
print(answer)
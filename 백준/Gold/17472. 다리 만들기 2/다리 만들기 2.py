from heapq import heappush, heappop
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b


def find(a):
    if p[a] == a:
        return a
    p[a] = find(p[a])
    return p[a]


n, m = map(int, input().split())
country = [input().split() for _ in range(n)]
island = 0
checked = [[False] * m for _ in range(n)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for i in range(n):
    for j in range(m):
        if country[i][j] == '1' and not checked[i][j]:
            island += 1
            checked[i][j] = True
            q = [(i, j)]
            country[i][j] = island
            while q:
                ci, cj = q.pop()
                for di, dj in d:
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < n and 0 <= nj < m and not checked[ni][nj] and country[ni][nj] == '1':
                        q.append((ni, nj))
                        checked[ni][nj] = True
                        country[ni][nj] = island
dist = [[11] * island for _ in range(island)]
checked = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if type(country[i][j]) == type(int()) and not checked[i][j]:
            num = country[i][j]
            q = [(i, j)]
            checked[i][j] = True
            while q:
                ci, cj = q.pop()
                for di, dj in d:
                    ni, nj = ci+di, cj+dj
                    if 0 <= ni < n and 0 <= nj < m and not checked[ni][nj]:
                        if country[ni][nj] == num:
                            q.append((ni, nj))
                            checked[ni][nj] = True
                        else:
                            cnt = 0
                            while True:
                                if 0 <= ni < n and 0 <= nj < m:
                                    if type(country[ni][nj]) == type(str()):
                                        ni += di
                                        nj += dj
                                        cnt += 1
                                    else:
                                        if cnt >= 2:
                                            dist[num - 1][country[ni][nj] - 1] = min(dist[num - 1][country[ni][nj] - 1], cnt)
                                        break
                                else:
                                    break
q = []
for i in range(island):
    for j in range(island):
        if dist[i][j] < 11:
            heappush(q, (dist[i][j], i, j))
p = list(range(island))
answer = 0
while q:
    bridge, i, j = heappop(q)
    if find(i) == find(j): continue
    union(i, j)
    answer += bridge
for i in range(island):
    find(i)
if sum(p) == 0:
    print(answer)
else:
    print(-1)
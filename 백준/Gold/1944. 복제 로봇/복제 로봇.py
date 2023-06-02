from collections import defaultdict, deque
from heapq import heappush, heappop
def find_parent(a):
    if table[a] != a:
        table[a] = find_parent(table[a])
    return table[a]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        table[b] = a
    else:
        table[a] = b

n, m = map(int, input().split())
maze = [list(input()) for _ in range(n)]
q = []
table = list(range(m+2))
index = defaultdict(int)
tmp = 1
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i in range(n):
    for j in range(n):
        if maze[i][j] == 'S' or maze[i][j] == 'K':
            if index[(i, j)] == 0:
                index[(i, j)] = tmp
                tmp += 1
            checked = [[True] * n for _ in range(n)]
            checked[i][j] = False
            tmpQ = deque([(i, j, 0)])
            rest_K = m
            while tmpQ and rest_K > 0:
                ci, cj, cnt = tmpQ.popleft()
                for di, dj in d:
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < n and 0 <= nj < n and checked[ni][nj]:
                        if maze[ni][nj] == '0':
                            tmpQ.append((ni, nj, cnt + 1))
                            checked[ni][nj] = False
                        elif maze[ni][nj] == 'K' or maze[ni][nj] == 'S':
                            tmpQ.append((ni, nj, cnt + 1))
                            checked[ni][nj] = False
                            rest_K -= 1
                            if index[(ni, nj)] == 0:
                                index[(ni, nj)] = tmp
                                tmp += 1
                            heappush(q, (cnt + 1, index[(i, j)], index[(ni, nj)]))
answer = 0
while q and m > 0:
    dist, a, b = heappop(q)
    pa = find_parent(a)
    pb = find_parent(b)
    if pa != pb:
        answer += dist
        union(a, b)
        m -= 1
if m > 0:
    print(-1)
else:
    print(answer)
import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    s, d = map(int, input().split())
    arr = defaultdict(list)
    for _ in range(m):
        u, v, p = map(int, input().split())
        arr[u].append((v, p))
    remove = defaultdict(set)
    memo = [['INF', set()] for _ in range(n)]
    memo[s][0] = 0
    q = []
    for v, p in arr[s]:
        heappush(q, (p, v, s))
    while q:
        dist, c, b = heappop(q)
        if memo[d][0] != 'INF' and dist > memo[d][0]:
            break
        if memo[c][0] == 'INF' or dist < memo[c][0]:
            memo[c] = [dist, {b}]
            for v, p in arr[c]:
                if memo[v][0] == 'INF' or dist + p <= memo[v][0]:
                    heappush(q, (dist + p, v, c))
        elif dist == memo[c][0]:
            memo[c][1].add(b)

    min_way = defaultdict(set)
    checked = [0] * n
    q = deque()
    for i in memo[d][1]:
        checked[d] = 1
        q.append((i, d))
    while q:
        u, v = q.popleft()
        min_way[u].add(v)
        if checked[u] == 0:
            for i in memo[u][1]:
                q.append((i, u))
        checked[u] = 1

    memo = ['INF'] * n
    q = []
    for v, p in arr[s]:
        if v not in min_way[s]:
            heappush(q, (p, v))
    memo[s] = 0
    answer = -1
    while q:
        dist, c = heappop(q)
        if c == d:
            answer = dist
            break
        if memo[c] == 'INF' or dist < memo[c]:
            memo[c] = dist
            for v, p in arr[c]:
                if v not in min_way[c] and (memo[v] == 'INF' or dist + p < memo[v]):
                    heappush(q, (dist + p, v))
    print(answer)
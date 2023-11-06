import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n, m, a, b, c = map(int, input().split())
a -= 1
b -= 1
road = [[] for _ in range(n)]
for _ in range(m):
    s, e, d = map(int, input().split())
    road[s-1].append((e-1, d))
    road[e-1].append((s-1, d))

q = []
for e, d in road[a]:
    if d <= c:
        heappush(q, (d, d, e))
# [max_d, sum_d]
dist = [11111111] * n
dist[a] = 0
answer = -1
while q:
    tmp, d_sum, s = heappop(q)
    if s == b:
        answer = tmp
        break
    for e, d in road[s]:
        if dist[e] > max(tmp, d) and d_sum + d <= c:
            dist[e] = max(tmp, d)
            heappush(q, (max(tmp, d), d_sum+d, e))
print(answer)
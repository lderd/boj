import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n, v, e = map(int, input().split())
a, b = map(int, input().split())
hs = list(map(int, input().split()))
arr = [[] for _ in range(v+1)]
for _ in range(e):
    i, j, l = map(int, input().split())
    arr[i].append((j, l))
    arr[j].append((i, l))

a_dist = [0] + [-1] * v
a_dist[a] = 0
q = [(0, a)]
while q:
    c_d, c = heappop(q)
    if a_dist[c] > c_d: continue
    for ne, d in arr[c]:
        if a_dist[ne] == -1 or c_d + d < a_dist[ne]:
            heappush(q, (c_d + d, ne))
            a_dist[ne] = c_d + d

b_dist = [0] + [-1] * v
b_dist[b] = 0
q = [(0, b)]
while q:
    c_d, c = heappop(q)
    if b_dist[c] > c_d: continue
    for ne, d in arr[c]:
        if b_dist[ne] == -1 or c_d + d < b_dist[ne]:
            heappush(q, (c_d + d, ne))
            b_dist[ne] = c_d + d

answer = 0
for h in hs:
    answer += a_dist[h] + b_dist[h]
print(answer)
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
v, m = map(int, input().split())
arr = [[] for _ in range(v+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))
j, s = map(int, input().split())

q = [(0, j)]
j_dist = [10000000] * (v+1)
j_dist[j] = 0
j_checked = set(range(1, v+1))
while q and j_checked:
    c_dist, c = heappop(q)
    if c not in j_checked: continue
    j_checked.remove(c)
    for n, d in arr[c]:
        if c_dist + d < j_dist[n]:
            heappush(q, (c_dist + d, n))
            j_dist[n] = c_dist + d

q = [(0, s)]
s_dist = [10000000] * (v+1)
s_dist[s] = 0
s_checked = set(range(1, v+1))
while q and s_checked:
    c_dist, c = heappop(q)
    if c not in s_checked: continue
    s_checked.remove(c)
    for n, d in arr[c]:
        if c_dist + d < s_dist[n]:
            heappush(q, (c_dist + d, n))
            s_dist[n] = c_dist + d

answer = -1
j_d = 10000000
s_d = 10000000
dist = 10000000
for i in range(1, v+1):
    if i == j or i == s: continue
    if j_dist[i] + s_dist[i] < dist:
        dist = j_dist[i] + s_dist[i]
for i in range(1, v+1):
    if i == j or i == s: continue
    a, b = j_dist[i], s_dist[i]
    if a > b: continue
    if a + b == dist:
        if a < j_d:
            answer = i
            j_d = a
            s_d = b
print(answer)
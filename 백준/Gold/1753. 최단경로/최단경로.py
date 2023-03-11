from collections import defaultdict
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
v, e = map(int, input().split())
s = int(input())
arr = defaultdict(list)
for _ in range(e):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
dist = ['INF'] * (v + 1)
q = [(0, s)]
check = set(range(1, v+1))
while q and check:
    c, a = heappop(q)
    if a in check:
        dist[a] = c
        check.remove(a)
        for b, w in arr[a]:
            if dist[b] == 'INF' or dist[b] > c + w:
                heappush(q, (c+w, b))
for i in range(1, v+1):
    print(dist[i])
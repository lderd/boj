# https://www.acmicpc.net/problem/14621
import sys
input = sys.stdin.readline
from heapq import heappop, heappush
def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


n, m = map(int, input().split())
sex = input().strip().split()
answer = 0
parent = list(range(n))
q = []
for _ in range(m):
    a, b, dist = map(int, input().split())
    heappush(q, (dist, a - 1, b - 1))
while q:
    dist, a, b = heappop(q)
    if sex[a] != sex[b] and find(a) != find(b):
        answer += dist
        union(a, b)
for i in range(n):
    if find(i) != 0:
        print(-1)
        break
else:
    print(answer)
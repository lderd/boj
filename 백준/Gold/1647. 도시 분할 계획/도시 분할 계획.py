from heapq import heappop, heappush
import sys
input = sys.stdin.readline
def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b


def find(a):
    if p[a] == a:
        return p[a]
    p[a] = find(p[a])
    return p[a]


n, m = map(int, input().split())
p = list(range(n))
l = n
q = []
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = max(a, b), min(a, b)
    heappush(q, (c, a-1, b-1))

answer = 0
while m and l > 2:
    c, a, b = heappop(q)
    m -= 1
    pa = find(a)
    pb = find(b)
    if pa != pb:
        union(pa, pb)
        l -= 1
        answer += c
print(answer)
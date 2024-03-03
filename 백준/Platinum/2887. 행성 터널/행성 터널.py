from heapq import heappop, heappush
import sys
input = sys.stdin.readline
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b


def find(a):
    if p[a] == a:
        return p[a]
    p[a] = find(p[a])
    return p[a]


n = int(input())
xp = []
yp = []
zp = []
for i in range(n):
    x, y, z = map(int, input().split())
    xp.append((x, i))
    yp.append((y, i))
    zp.append((z, i))
q = []
xp.sort()
yp.sort()
zp.sort()
for i in range(n-1):
    heappush(q, (xp[i+1][0] - xp[i][0], xp[i][1], xp[i+1][1]))
    heappush(q, (yp[i+1][0] - yp[i][0], yp[i][1], yp[i+1][1]))
    heappush(q, (zp[i+1][0] - zp[i][0], zp[i][1], zp[i+1][1]))
p = list(range(n))
ps = n
answer = 0
while ps > 1:
    dist, a, b = heappop(q)
    pa, pb = find(a), find(b)
    if pa != pb:
        union(pa, pb)
        answer += dist
        ps -= 1
print(answer)
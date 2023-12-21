from heapq import heappop, heappush
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


n, k = map(int, input().split())
arr = [[] for _ in range(n)]
q = []
for _ in range(k):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))
    q.append((c, a, b))
q.sort()
p = list(range(n))
rest = n
idx = 0
total_cost = 0
info = [[] for _ in range(n)]
while rest > 1:
    d, a, b = q[idx]
    pa = find(a)
    pb = find(b)
    if pa != pb:
        union(a, b)
        info[a].append((b, d))
        info[b].append((a, d))
        total_cost += d
        rest -= 1
    idx += 1

not_checked = set(range(n))
dist = [total_cost+1] * n
q = [(0, 0)]
dist[0] = 0
last = 0
while q and not_checked:
    d, a = heappop(q)
    if a not in not_checked: continue
    not_checked.remove(a)
    last = a
    for b, dd in info[a]:
        if d+dd < dist[b]:
            heappush(q, (d+dd, b))
            dist[b] = d+dd

not_checked = set(range(n))
dist = [total_cost+1] * n
q = [(0, last)]
dist[last] = 0
max_cost = 0
while q and not_checked:
    d, a = heappop(q)
    if a not in not_checked: continue
    not_checked.remove(a)
    max_cost = d
    for b, dd in info[a]:
        if d+dd < dist[b]:
            heappush(q, (d+dd, b))
            dist[b] = d+dd
print(total_cost)
print(max_cost)
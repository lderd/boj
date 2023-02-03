from heapq import heappop, heappush
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
dist = [9876543210] * (n+1)
dist[1] = 0
q = []
heappush(q, (0, 1))
checked = set(range(1, n+1))
while checked and q:
    d, s = heappop(q)
    if s == n:
        print(d)
        break
    if s in checked:
        checked.remove(s)
        for b, c in graph[s]:
            if d + c < dist[b]:
                dist[b] = d + c
                heappush(q, (d+c, b))
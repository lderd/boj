from heapq import heappop, heappush
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, d = map(int, input().split())
    graph[s].append([e, d])

s, e = map(int, input().split())
cost = [9876543210] * (n + 1)
checked = set(range(1, n+1))

h = []
heappush(h, [0, s])

cost[s] = 0
while h and checked:
    cost_, cs = heappop(h)
    if cs in checked:
        checked.remove(cs)
    else:
        continue
    if cs == e:
        break
    for ce, d in graph[cs]:
        if cost[ce] > cost_ + d:
            heappush(h, [cost_ + d, ce])
            cost[ce] = cost_ + d
print(cost[e])
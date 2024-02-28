import sys

input = sys.stdin.readline

import heapq

v, m = map(int, input().split())

inf = int(1e10)

arr = [[] for i in range(v + 1)]

distance_j = [inf] * (v + 1)
distance_s = [inf] * (v + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

j, s = map(int, input().split())


def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in arr[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(j, distance_j)
dijkstra(s, distance_s)

min = inf
for i in range(1, v + 1):
    if i != j and i != s:
        if distance_j[i] + distance_s[i] < min:
            min = distance_j[i] + distance_s[i]

x = inf
# y = inf
result = -1

for i in range(v, 0, -1):
    if i != j and i != s:
        if distance_j[i] <= distance_s[i] and distance_j[i] + distance_s[i] == min:
            if distance_j[i] <= x:
                x = distance_j[i]
                # y = distance_s[i]
                result = i

print(result)

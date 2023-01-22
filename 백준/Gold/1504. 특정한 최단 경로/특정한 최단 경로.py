from heapq import heappush, heappop
# 정점n, 간선e
n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    s, d, dist = map(int, input().split())
    graph[s].append([d, dist])
    graph[d].append([s, dist])

v1, v2 = map(int, input().split())
waypoint = [[1, v1, v2, n], [1, v2, v1, n]]

answer = 9876543210

for way in range(2):
    tmp = 0
    for i in range(3):
        min_dist = [9876543210] * (n+1)
        h = []

        for d, dist in graph[waypoint[way][i]]:
            min_dist[d] = dist
            heappush(h, [dist, d])

        checked = set(range(1, n+1))

        min_dist[waypoint[way][i]] = 0
        checked.remove(waypoint[way][i])

        while h and checked:
            dist_, s = heappop(h)
            if s == waypoint[way][i+1]:
                break

            if s in checked:
                checked.remove(s)
                for d, dist in graph[s]:
                    if min_dist[d] > dist_ + dist:
                        heappush(h, [dist_ + dist, d])
                        min_dist[d] = dist_ + dist

        if min_dist[waypoint[way][i+1]] < 9876543210:
            tmp += min_dist[waypoint[way][i+1]]
        else:
            tmp = -1
            break
    if answer > tmp:
        answer = tmp
print(-1) if answer == 9876543210 else print(answer)
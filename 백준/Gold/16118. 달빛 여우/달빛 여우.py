from heapq import heappop, heappush
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
road = [[] for _ in range(n)]
for _ in range(m):
    a, b, d = map(int, input().split())
    road[a-1].append((b-1, 2*d))
    road[b-1].append((a-1, 2*d))
fox_dist = [2000000000] * n
fox_dist[0] = 0
fox_q = [(0, 0)]
while fox_q:
    dist, num = heappop(fox_q)
    if fox_dist[num] < dist: continue
    for b, d in road[num]:
        new_dist = dist + d
        if fox_dist[b] > new_dist:
            fox_dist[b] = new_dist
            heappush(fox_q, (new_dist, b))
wolf_dist = [[2000000000, 2000000000] for _ in range(n)]
wolf_dist[0][0] = 0
# 걸어왔으면 0, 뛰어왔으면 1
wolf_q = [(0, 0, 0)]
while wolf_q:
    dist, num, run = heappop(wolf_q)
    if wolf_dist[num][run] < dist: continue
    if run:
        for b, d in road[num]:
            new_dist = dist + d * 2
            if wolf_dist[b][0] > new_dist:
                wolf_dist[b][0] = new_dist
                heappush(wolf_q, (new_dist, b, 0))
    else:
        for b, d in road[num]:
            new_dist = dist + d // 2
            if wolf_dist[b][1] > new_dist:
                wolf_dist[b][1] = new_dist
                heappush(wolf_q, (new_dist, b, 1))
answer = 0
for i in range(1, n):
    if fox_dist[i] < min(wolf_dist[i]):
        answer += 1
print(answer)
'''
 0   1   2   3
0 1 2 3 4 5 6 7
'''
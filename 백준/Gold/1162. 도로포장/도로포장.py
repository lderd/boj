import sys
from heapq import heappop, heappush
from collections import defaultdict

input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = defaultdict(list)
for _ in range(m):
    a, b, d = map(int, input().split())
    arr[a-1].append((b-1, d))
    arr[b-1].append((a-1, d))

memo = [[-1] * (k+1) for _ in range(n)]
memo[0] = [0] * (k+1)

q = []
for nxt, d in arr[0]:
    heappush(q, (d, 0, nxt))
    heappush(q, (0, 1, nxt))

while q:
    dist, cnt, city = heappop(q)
    if memo[city][cnt] == -1 or memo[city][cnt] > dist:
        memo[city][cnt] = dist
        if cnt < k:
            for nxt, d in arr[city]:
                if memo[nxt][cnt] == -1 or dist + d < memo[nxt][cnt]:
                    heappush(q, (dist + d, cnt, nxt))
                if memo[nxt][cnt + 1] == -1 or dist < memo[nxt][cnt + 1]:
                    heappush(q, (dist, cnt+1, nxt))
        else:
            for nxt, d in arr[city]:
                if memo[nxt][cnt] == -1 or dist + d < memo[nxt][cnt]:
                    heappush(q, (dist + d, cnt, nxt))
answer = -1
for i in range(k+1):
    if answer == -1 and memo[n-1][i] >= 0:
        answer = memo[n-1][i]
    elif answer > memo[n-1][i]:
        answer = memo[n-1][i]
print(answer)
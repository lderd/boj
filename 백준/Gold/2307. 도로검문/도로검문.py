import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[] for _ in range(n)]
for _ in range(m):
    a, b, t = map(int, input().split())
    arr[a-1].append((b-1, t))
    arr[b-1].append((a-1, t))
dist = [-1] * n
dist[0] = 0
q = [(0, 0)]
while q:
    t, e = heappop(q)
    if dist[e] > t: continue
    if e == n - 1:
        break
    for next_n, next_t in arr[e]:
        if dist[next_n] == -1 or dist[next_n] > t + next_t:
            dist[next_n] = t + next_t
            heappush(q, (t + next_t, next_n))
out_time = dist[n-1]
if out_time == -1:
    print(0)
    sys.exit()
checked = set()
answer = 0
for a in range(n):
    for b, _ in arr[a]:
        if (min(a, b), max(a, b)) in checked: continue
        checked.add((min(a, b), max(a, b)))
        dist = [-1] * n
        dist[0] = 0
        q = [(0, 0)]
        while q:
            t, e = heappop(q)
            if dist[e] > t: continue
            if e == n - 1:
                break
            for next_n, next_t in arr[e]:
                if (e == a and next_n == b) or (e == b and next_n == a): continue
                if dist[next_n] == -1 or dist[next_n] > t + next_t:
                    dist[next_n] = t + next_t
                    heappush(q, (t + next_t, next_n))
        block_time = dist[n-1]
        if block_time == -1:
            print(-1)
            sys.exit()
        if answer < block_time - out_time:
            answer = block_time - out_time
print(answer)
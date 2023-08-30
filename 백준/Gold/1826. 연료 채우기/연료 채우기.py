from heapq import heappop, heappush
import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))
arr.sort()
l, p = map(int, input().split())
q = []
cnt = 0
for a, b in arr:
    while q and p < a:
        p -= heappop(q)
        cnt += 1
    if p >= l:
        break
    if p < a:
        cnt = -1
        break
    else:
        heappush(q, -b)
while q and p < l:
    p -= heappop(q)
    cnt += 1
if p >= l:
    print(cnt)
else:
    print(-1)
from heapq import heappush, heappop
from collections import defaultdict
n, m, x = map(int, input().split())
info = defaultdict(list)
for _ in range(m):
    a, b, t = map(int, input().split())
    info[a-1].append((b-1, t))
arr = [[987654321] * n for _ in range(n)]
for i in range(n):
    q = []
    checked = set(range(n))
    checked.remove(i)
    for b, t in info[i]:
        heappush(q, (t, b))
    while checked and q:
        t, b = heappop(q)
        if b in checked:
            checked.remove(b)
            arr[i][b] = t
            if b == x-1:
                break
            for bb, tt in info[b]:
                if t + tt < arr[i][bb]:
                    heappush(q, (t + tt, bb))
answer = 0
for i in range(n):
    if i == x-1:
        continue
    tmp = arr[i][x-1] + arr[x-1][i]
    if tmp > answer:
        answer = tmp
print(answer)
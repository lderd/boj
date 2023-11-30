from heapq import heappop, heappush
n, l = map(int, input().split())
a = list(map(int, input().split()))
q = []
answer = []
for i in range(n):
    heappush(q, (a[i], i))
    while True:
        v, vi = q[0]
        if vi < i - l + 1:
            heappop(q)
        else:
            answer.append(v)
            break
print(*answer)
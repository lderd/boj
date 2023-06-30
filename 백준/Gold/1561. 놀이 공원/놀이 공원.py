import sys
from heapq import heappop, heappush
n, m = map(int, input().split())
time_table = list(map(int, input().split()))
if n <= m:
    print(n)
    sys.exit()
s = 0
e = 200000000000001
n -= m
while s <= e:
    mid = (s + e) // 2
    tmp = 0
    for i in range(m):
        tmp += mid // time_table[i]
    if tmp < n:
        s = mid + 1
    else:
        e = mid - 1
q = []
cnt = 0
for i in range(m):
    cnt += e // time_table[i]
    heappush(q, (time_table[i] - e % time_table[i], i))
while cnt < n:
    time, index = heappop(q)
    cnt += 1
    if cnt >= n:
        print(index + 1)
    heappush(q, (time + time_table[index], index))
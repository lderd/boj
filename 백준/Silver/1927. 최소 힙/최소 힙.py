from heapq import heappop, heappush
import sys
input = sys.stdin.readline
n = int(input())
q = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if q:
            answer = heappop(q)
            print(answer)
        else:
            print(0)
    else:
        heappush(q, x)
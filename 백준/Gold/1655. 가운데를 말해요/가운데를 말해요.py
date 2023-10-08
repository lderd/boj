from heapq import heappush, heappop
import sys
input = sys.stdin.readline
n = int(input())
small = []
big = []
answer = int(input())
print(answer)
for _ in range(n - 1):
    number = int(input())
    if number >= answer:
        heappush(big, number)
    else:
        heappush(small, -number)
    if len(small) == len(big) or len(small) + 1 == len(big):
        print(answer)
    else:
        if len(small) > len(big):
            heappush(big, answer)
            answer = -heappop(small)
        else:
            heappush(small, -answer)
            answer = heappop(big)
        print(answer)
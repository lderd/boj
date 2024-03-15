from heapq import heappop, heappush
import sys
input = sys.stdin.readline
c, n = map(int, input().split())
cow = []
for _ in range(c):
    cow.append(int(input()))
chicken = []
for _ in range(n):
    a, b = map(int, input().split())
    chicken.append((a, b))
cow.sort()
chicken.sort()
chickenQ = []
cow_num = 0
chicken_num = 0
answer = 0
while cow_num < c:
    while chicken_num < n:
        a, b = chicken[chicken_num]
        if a <= cow[cow_num]:
            heappush(chickenQ, b)
            chicken_num += 1
        else:
            break
    while chickenQ:
        b = chickenQ[0]
        if cow[cow_num] <= b:
            heappop(chickenQ)
            answer += 1
            break
        elif cow[cow_num] > b:
            heappop(chickenQ)
    cow_num += 1
print(answer)
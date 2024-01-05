from heapq import heappop, heappush
n = int(input())
pack = []
for _ in range(n):
    heappush(pack, int(input()))
answer = 0
while pack:
    a = heappop(pack)
    if pack:
        b = heappop(pack)
        answer += a + b
        heappush(pack, a+b)
print(answer)
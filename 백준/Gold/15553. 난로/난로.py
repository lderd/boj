from heapq import heappop, heappush
N, K = map(int, input().split())
arr = []
before = int(input())
for _ in range(N-1):
    after = int(input())
    tmp = after - before
    heappush(arr, tmp)
    before = after
answer = N
cnt = N
while cnt > K:
    cnt -= 1
    answer -= 1
    tmp = heappop(arr)
    answer += tmp
print(answer)
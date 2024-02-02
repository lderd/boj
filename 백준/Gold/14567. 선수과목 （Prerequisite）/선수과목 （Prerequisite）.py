import sys
input = sys.stdin.readline
n, m = map(int, input().split())
answer = [1] * (n+1)
schedule = [tuple(map(int, input().split())) for _ in range(m)]
schedule.sort()
for a, b in schedule:
    answer[b] = max(answer[a]+1, answer[b])
for i in range(1, n+1):
    print(answer[i], end=' ')
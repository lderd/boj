n = int(input())
answer = 0
oil = 1000000001
dist = 0
road = list(map(int, input().split()))
cost = list(map(int, input().split()))
for i in range(n-1):
    if oil > cost[i]:
        answer += oil * dist
        dist = 0
        oil = cost[i]
    dist += road[i]
answer += oil * dist
print(answer)
import sys
input = sys.stdin.readline
n, s, e, m = map(int, input().split())
roads = [[] for _ in range(n)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    roads[a].append((b, cost))
city = list(map(int, input().split()))
# 최대가 되는 경로로 도착을 찾아 감
# bfs인데 순환이 발생하는지(순환하면 손해인 경우와 이득인 경우로 나뉨), 도착이 가능한지 등을 포함하여 탐색
'''
현재도시, money[], check[](한번은 체크했더라도 감. 2번은 안감)
'''
inf = 1000000000
money = [-inf] * n
money[s] = city[s]
check = [0] * n
check[s] = 1
q = []
for post, cost in roads[s]:
    if money[post] < money[s] - cost + city[post]:
        money[post] = money[s] - cost + city[post]
        q.append((post, money[post], 0))
while q:
    current, c_money, idx = q.pop()
    check[current] -= 1
    if c_money < money[current]: continue
    if idx < len(roads[current]):
        q.append((current, c_money, idx+1))
        check[current] += 1
        post, cost = roads[current][idx]
        if money[post] < c_money - cost + city[post] or c_money == inf:
            if check[post] < 1:
                if c_money == inf:
                    money[post] = inf
                else:
                    money[post] = c_money - cost + city[post]
                q.append((post, money[post], 0))
                check[post] += 1
            elif check[post] < 2:
                money[post] = inf
                q.append((post, money[post], 0))
                check[post] += 1
answer = money[e]
if answer == -inf:
    print('gg')
elif answer == inf:
    print('Gee')
else:
    print(answer)
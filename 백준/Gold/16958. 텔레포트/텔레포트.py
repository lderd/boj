import sys

from pprint import pprint

input = sys.stdin.readline

n, t = map(int, input().split())

inf = int(1e9)

arr = [[inf] * (n + 1) for _ in range(n + 1)]

city = [0]
for _ in range(n):
    # s : 1 -> 특별한 도시 텔레포트 가능 0 -> 불가능
    # x,y 도시 좌표
    s, x, y = map(int, input().split())
    city.append((s, x, y))

near = [0] * (n + 1)
for i in range(1, n + 1):
    # 이 도시가 텔포 불가능한 지점이라면
    # 가장 가까운 텔포지점을 찾자
    if city[i][0] == 0:
        minvalue = inf
        for j in range(1, n + 1):
            if city[j][0] == 1 and abs(city[i][1] - city[j][1]) + abs(city[i][2] - city[j][2]) < minvalue:
                minvalue = abs(city[i][1] - city[j][1]) + abs(city[i][2] - city[j][2])
                # near[i] = j
                near[i] = minvalue
# 경우의 수 4가지

# 둘다 텔포 불가능
# -> 직선거리와
# 시작점에서 가장 가까운 텔포지점이동후 텔포
# 도착점에서 가장 가까운 텔포지점 이동후 도착지까지 움직이기 와 비교하기
# 둘다 텔포 가능
# -> 텔포 타는게 가장 빠르다
# 시작점만 텔포 가능
# -> 도착점에서 가장 가까운 텔포지점으로 텔포타자 그리고 그냥 직선 거리와 비교하자
# 도착점만 텔포 가능
# -> 시작점에서 가장 가까운 텔포지점으로 텔포타자 그리고 그냥 직선 거리와 비교하자

# print(city)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        s1, x1, y1 = city[i]
        s2, x2, y2 = city[j]

        if i == j:
            arr[i][j] = 0
        else:
            if s1 == 0 and s2 == 0:
                # arr[i][j] = min(abs(x1 - x2) + abs(y1 - y2),
                #                 abs(x1 - city[near[i]][1]) + abs(y1 - city[near[i]][2]) + abs(
                #                     x2 - city[near[j]][1]) + abs(y2 - city[near[j]][2]) + 2 * t)
                arr[i][j] = min(abs(x1 - x2) + abs(y1 - y2), near[i] + near[j] + t)
            elif s1 == 0 and s2 == 1:
                # arr[i][j] = min(abs(x1 - x2) + abs(y1 - y2),
                #                 abs(x1 - city[near[i]][1]) + abs(y1 - city[near[i]][2]) + t)
                arr[i][j] = min(abs(x1 - x2) + abs(y1 - y2), near[i]+ t)
            elif s1 == 1 and s2 == 0:
                # arr[i][j] = min(abs(x1 - x2) + abs(y1 - y2),
                #                 abs(x2 - city[near[j]][1]) + abs(y2 - city[near[j]][2]) + t)
                arr[i][j] = min(abs(x1 - x2) + abs(y1 - y2), near[j] + t)
            elif s1 == 1 and s2 == 1:
                arr[i][j] = min(abs(x1 - x2) + abs(y1 - y2), t)

m = int(input())


for _ in range(m):
    a, b = map(int, input().split())

    print(arr[a][b])

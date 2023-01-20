# 테케 수
t = int(input())
for _ in range(t):
    # 층
    k = int(input())
    # 호수
    n = int(input())
    floor = list(range(1, n+1))
    for i in range(k):
        tmp_floor = [1]
        for j in range(1, n):
            tmp_floor.append(tmp_floor[j-1]+floor[j])
        floor = tmp_floor
    print(floor[n-1])
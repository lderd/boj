from heapq import heappop, heappush
T = int(input())
for _ in range(T):
    # 교차로, 도로, 목적지 후보 수
    n, m, t = map(int, input().split())
    # 출발지, g와 h사이의 도로를 지나갔다
    s, g, h = map(lambda x:int(x) - 1, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a-1].append((b-1, d))
        graph[b-1].append((a-1, d))
    hubo = set()
    for _ in range(t):
        hubo.add(int(input()))
    q = [(0, True, s)]
    dist = [10000000000] * n
    dist[s] = 0
    possible = set()
    checked = set()
    while q:
        d, tf, a = heappop(q)
        if d == dist[a]:
            if not tf:
                possible.add(a + 1)
            if a in checked: continue
            checked.add(a)
            for b, dd in graph[a]:
                if d + dd <= dist[b]:
                    dist[b] = d + dd
                    if (g == a and h == b) or (g == b and h == a):
                        heappush(q, (d+dd, False, b))
                    else:
                        heappush(q, (d+dd, tf, b))
    print(*sorted(hubo & possible))
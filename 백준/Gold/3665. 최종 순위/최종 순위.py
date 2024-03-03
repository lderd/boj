import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    ts = list(map(int, input().split()))
    before_rank = [0] * (n + 1)
    arr = [set() for _ in range(n + 1)]
    tmp = set()
    for i in range(n-1, -1, -1):
        before_rank[ts[i]] = i
        arr[ts[i]] |= tmp
        tmp.add(ts[i])
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if before_rank[a] < before_rank[b]:
            a, b = b, a
        # a가 뒤에 있음
        arr[a].add(b)
        arr[b].remove(a)
    cnt = [0] * (n + 1)
    for i in range(1, n+1):
        for j in arr[i]:
            cnt[j] += 1
    answer = []
    ans_l = 0
    q = []
    l = 0
    for i in range(1, n+1):
        if cnt[i] == 0:
            q.append(i)
            l += 1
    while l == 1:
        c = q.pop()
        l -= 1
        answer.append(c)
        ans_l += 1
        for j in arr[c]:
            cnt[j] -= 1
            if cnt[j] == 0:
                q.append(j)
                l += 1
    if ans_l < n:
        print('IMPOSSIBLE')
    else:
        print(*answer)
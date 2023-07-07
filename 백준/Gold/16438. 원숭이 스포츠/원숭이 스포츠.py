def solve(s, e, d):
    if s >= e:
        return
    mid = (s + e) // 2
    answer[d].append((s, mid))
    solve(s, mid, d + 1)
    solve(mid + 1, e, d + 1)


n = int(input())
answer = [[] for _ in range(7)]
solve(0, n-1, 0)
for i in range(7):
    tmp = ['B'] * n
    if answer[i]:
        for s, e in answer[i]:
            for j in range(s, e + 1):
                tmp[j] = 'A'
    else:
        tmp[-1] = 'A'
    print(''.join(tmp))
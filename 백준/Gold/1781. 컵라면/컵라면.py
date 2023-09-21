import sys
input = sys.stdin.readline
def find(a):
    if p[a] != a:
        p[a] = find(p[a])
    return p[a]


def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa < pb:
        p[pb] = pa
    elif pb < pa:
        p[pa] = pb


n = int(input())
dead_cup = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x:[-x[1]])
p = list(range(n + 1))
tmp = [0] * (n + 1)
answer = 0
for limit, cnt in dead_cup:
    idx = find(limit)
    if idx > 0:
        answer += cnt
        tmp[idx] = cnt
        union(limit, idx - 1)
print(answer)
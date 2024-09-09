import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b


def find(a):
    if p[a] == a:
        return a
    p[a] = find(p[a])
    return p[a]


v, e = map(int, input().split())
answer = 0
p = list(range(v))
q = []
for _ in range(e):
    a, b, c = map(int, input().split())
    q.append((c, a-1, b-1))
q.sort()
rest = v - 1
for j in range(e):
    c, a, b = q[j]
    a = find(a)
    b = find(b)
    if a != b:
        rest -= 1
        answer += c
        union(a, b)
    if rest == 0:
        break
print(answer)
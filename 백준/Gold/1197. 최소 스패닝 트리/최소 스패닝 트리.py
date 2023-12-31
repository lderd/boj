import sys
input = sys.stdin.readline
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b


def find(a):
    if p[a] == a:
        return p[a]
    p[a] = find(p[a])
    return p[a]


v, e = map(int, input().split())
answer = 0
p = list(range(v+1))
q = []
for _ in range(e):
    a, b, c = map(int, input().split())
    q.append((c, a-1, b-1))
q.sort()
for j in range(e):
    c, a, b = q[j]
    a = find(a)
    b = find(b)
    if a != b:
        answer += c
        union(a, b)
print(answer)
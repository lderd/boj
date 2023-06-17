import sys
def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


input = sys.stdin.readline
t = int(input())
for i in range(1, t + 1):
    n = int(input())
    parent = list(range(n))
    k = int(input())
    for _ in range(k):
        a, b = map(int, input().split())
        union(a, b)
    m = int(input())
    print(f'Scenario {i}:')
    for _ in range(m):
        u, v = map(int, input().split())
        if find(u) == find(v):
            print(1)
        else:
            print(0)
    print()
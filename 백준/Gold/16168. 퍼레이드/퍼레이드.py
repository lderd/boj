def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

v, e = map(int, input().split())
spots = [0] * (v+1)
parent = list(range(v+1))
for _ in range(e):
    a, b = map(int, input().split())
    spots[a] += 1
    spots[b] += 1
    union(a, b)
odd = 0
cnt = set()
for i in range(1, v+1):
    if spots[i] % 2:
        odd += 1
    cnt.add(find(i))
if (odd == 0 or odd == 2) and len(cnt) == 1:
    print('YES')
else:
    print('NO')
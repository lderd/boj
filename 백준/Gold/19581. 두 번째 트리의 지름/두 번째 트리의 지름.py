from heapq import heappop, heappush
n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n-1):
    a, b, d = map(int, input().split())
    tree[a-1].append((b-1, d))
    tree[b-1].append((a-1, d))
q = [(0, 0)]
checked = set(range(n))
dist = [20000000000] * n
one_of_end = 0
while q and checked:
    d, a = heappop(q)
    if a in checked:
        checked.remove(a)
        dist[a] = d
        one_of_end = a
        for b, dd in tree[a]:
            if b in checked and d + dd < dist[b]:
                heappush(q, (d+dd, b))

q = [(0, one_of_end)]
checked = set(range(n))
dist = [20000000000] * n
the_other_of_end = 0
while q and checked:
    d, a = heappop(q)
    if a in checked:
        checked.remove(a)
        dist[a] = d
        the_other_of_end = a
        for b, dd in tree[a]:
            if b in checked and d + dd < dist[b]:
                heappush(q, (d+dd, b))
first = [0, 0, 0]
second = [0, 0, 0]
for i in range(n):
    if dist[i] >= first[0]:
        second = first
        first = [dist[i], min(i, one_of_end), max(i, one_of_end)]
    elif dist[i] > second[0]:
        second = [dist[i], min(i, one_of_end), max(i, one_of_end)]
q = [(0, the_other_of_end)]
checked = set(range(n))
dist = [20000000000] * n
while q and checked:
    d, a = heappop(q)
    if a in checked:
        checked.remove(a)
        dist[a] = d
        for b, dd in tree[a]:
            if b in checked and d + dd < dist[b]:
                heappush(q, (d+dd, b))
for i in range(n):
    if dist[i] >= first[0] and (first[1] != min(i, the_other_of_end) or first[2] != max(i, the_other_of_end)):
        second = first
        first = [dist[i], min(i, the_other_of_end), max(i, the_other_of_end)]
    elif dist[i] > second[0] and (first[1] != min(i, the_other_of_end) or first[2] != max(i, the_other_of_end)):
        second = [dist[i], min(i, the_other_of_end), max(i, the_other_of_end)]
print(second[0])
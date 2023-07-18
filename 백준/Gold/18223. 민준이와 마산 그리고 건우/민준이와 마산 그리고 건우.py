from heapq import heappop, heappush
v, e, p = map(int, input().split())
arr = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))
s_to_v = 50000001
checked = set(range(1, v + 1))
q = [(0, 1)]
while q:
    d, now = heappop(q)
    if now not in checked: continue
    checked.remove(now)
    if now == v:
        s_to_v = d
        break
    for next, nd in arr[now]:
        if next in checked:
            heappush(q, (d + nd, next))

p_to_s = 50000001
p_to_v = 50000001
if p == 1 or p == v:
    p_to_s = 0
    p_to_v = 0
checked = set(range(1, v + 1))
q = [(0, p)]
while q and (p_to_s == 50000001 or p_to_v == 50000001):
    d, now = heappop(q)
    if now not in checked: continue
    checked.remove(now)
    if now == v:
        p_to_v = d
    if now == 1:
        p_to_s = d
    for next, nd in arr[now]:
        if next in checked:
            heappush(q, (d + nd, next))
if s_to_v >= p_to_s + p_to_v:
    print('SAVE HIM')
else:
    print('GOOD BYE')
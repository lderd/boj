import sys
input = sys.stdin.readline

v = int(input())
tree = [[] for _ in range(v)]
answer = [0, 0]
for _ in range(v):
    s, *info = map(int, input().split())
    tree[s-1] = info
q = []
q.append((0, 0, 0, {0}))
while q:
    s, dist, idx, checked = q.pop()
    if dist > answer[0]:
        answer = [dist, s]
    e = tree[s][idx] - 1
    if e == -2: continue
    q.append((s, dist, idx + 2, checked))
    if e not in checked:
        d = tree[s][idx+1]
        q.append((e, dist + d, 0, checked | {e}))
q.append((answer[1], 0, 0, {answer[1]}))
answer = 0
while q:
    s, dist, idx, checked = q.pop()
    if dist > answer:
        answer = dist
    e = tree[s][idx] - 1
    if e == -2: continue
    q.append((s, dist, idx + 2, checked))
    if e not in checked:
        d = tree[s][idx+1]
        q.append((e, dist + d, 0, checked | {e}))

print(answer)
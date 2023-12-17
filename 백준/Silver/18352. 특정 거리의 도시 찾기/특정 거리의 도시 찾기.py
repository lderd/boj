from collections import deque
n, m, k, x = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
q = deque([(x, 0)])
answer = []
checked = {x}
while q:
    a, cnt = q.popleft()
    if cnt >= k:
        answer.append(a)
        continue
    for b in arr[a]:
        if b not in checked:
            checked.add(b)
            q.append((b, cnt+1))
if answer:
    answer.sort()
    for ans in answer:
        print(ans)
else:
    print(-1)
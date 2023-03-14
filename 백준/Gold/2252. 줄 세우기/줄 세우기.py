from collections import defaultdict, deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = defaultdict(list)
cnt = defaultdict(int)
checked = set(range(1, n+1))
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    cnt[b] += 1
    if b in checked:
        checked.remove(b)
q = deque()
for a in checked:
    q.append(a)
answer = []
while q:
    a = q.popleft()
    answer.append(a)
    for b in arr[a]:
        cnt[b] -= 1
        if cnt[b] == 0:
            q.append(b)
print(*answer)
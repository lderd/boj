from collections import deque
n = int(input())
towers = list(map(int, input().split()))
q = deque()
answer = []
for i in range(n):
    while q:
        h, idx = q[-1]
        if h > towers[i]:
            answer.append(idx)
            break
        else:
            q.pop()
    if not q:
        answer.append(0)
    q.append((towers[i], i+1))
print(*answer)
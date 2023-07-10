from collections import deque
n = int(input())
answer = 0
q = deque()
for _ in range(n):
    x, y = map(int, input().split())
    while q:
        if q[-1] > y:
            q.pop()
            answer += 1
        else:
            break
    if q:
        if q[-1] < y:
            q.append(y)
    else:
        q.append(y)
while q:
    y = q.pop()
    if y > 0:
        answer += 1
print(answer)

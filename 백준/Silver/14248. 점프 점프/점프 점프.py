from collections import deque
q = deque()
n = int(input())
arr = list(map(int, input().split()))
start = int(input())
q.append(start-1)
checked = set()
checked.add(start-1)
answer = 1
while q:
    s = q.popleft()
    for i in [-1, 1]:
        tmp = s + arr[s] * i
        if 0 <= tmp < n and tmp not in checked:
            checked.add(tmp)
            q.append(tmp)
            answer += 1
print(answer)
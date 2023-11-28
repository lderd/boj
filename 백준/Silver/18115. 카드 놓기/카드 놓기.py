from collections import deque
n = int(input())
answer = deque()
a = input().split()
number = 1
for i in range(n-1, -1, -1):
    if a[i] == '1':
        answer.appendleft(number)
    elif a[i] == '2':
        tmp = answer.popleft()
        answer.appendleft(number)
        answer.appendleft(tmp)
    else:
        answer.append(number)
    number += 1
print(*answer)
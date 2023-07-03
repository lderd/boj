from collections import deque
n, k = map(int, input().split())
numbers = input()
answer = deque()
cnt = 0
for i in numbers:
    while answer and cnt < k and answer[-1] < i:
        answer.pop()
        cnt += 1
    answer.append(i)
print(''.join(answer)[:n-k])

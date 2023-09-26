import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
q = deque([(-1, 0)])
answer = 0
for i in range(n):
    h = int(input())
    while True:
        last_i, last_h = q[-1]
        if last_h <= h:
            q.append((i, h))
            break
        q.pop()
        llast_i, llast_h = q[-1]
        tmp = (i - llast_i - 1) * last_h
        if answer < tmp:
            answer = tmp
h = 0
while q:
    last_i, last_h = q.pop()
    if last_h == h: continue
    llast_i, llast_h = q[-1]
    tmp = (n - llast_i - 1) * last_h
    if answer < tmp:
        answer = tmp
print(answer)
'''
7
2
1
3
2
1
2
2

8
2
1
2
2
1
0
2
2
'''